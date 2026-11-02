
import os
import tempfile
from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_date, parse_time
from django.views.decorators.http import require_POST

from .forms import EventForm, SignUpForm
from .models import Event, Task
from .checklists import get_checklist

from .document_reader import (
    extract_text,
    find_date,
    find_time,
    find_event_title,
    find_venue,
    find_description,
    find_checklist_items,
)


# --------------------------------------------------
# DEFAULT EVENT DESCRIPTIONS
# --------------------------------------------------

def get_default_description(event_title, event_type):

    event_name = (
        event_type or event_title or ""
    ).strip().lower()

    if "wedding" in event_name or "marriage" in event_name:
        return (
            "A beautiful celebration of love and togetherness. "
            "Join family and friends to celebrate the beginning "
            "of a wonderful new journey."
        )

    elif "birthday" in event_name:
        return (
            "A joyful birthday celebration filled with happiness, "
            "laughter, and special moments. Join family and friends "
            "to make the day memorable."
        )

    elif "engagement" in event_name:
        return (
            "A special celebration marking the beginning of "
            "a beautiful journey together. Join loved ones "
            "for a memorable engagement ceremony."
        )

    elif "anniversary" in event_name:
        return (
            "A lovely celebration of togetherness, love, "
            "and cherished memories. Join family and friends "
            "to celebrate this special milestone."
        )

    elif "workshop" in event_name:
        return (
            "An interactive learning event designed to develop "
            "knowledge and practical skills. Participants will "
            "explore useful concepts and activities."
        )

    elif "seminar" in event_name:
        return (
            "An informative event featuring discussions and "
            "knowledge sharing on an important topic. "
            "Participants can learn and exchange ideas."
        )

    elif "conference" in event_name:
        return (
            "A professional gathering bringing people together "
            "to share knowledge, discuss ideas, and explore "
            "important topics and opportunities."
        )

    elif "farewell" in event_name:
        return (
            "A heartfelt gathering to celebrate memories, "
            "express gratitude, and wish someone success "
            "and happiness in their next journey."
        )

    elif "reunion" in event_name:
        return (
            "A wonderful opportunity to reconnect with friends, "
            "share memories, and celebrate the bonds "
            "that bring everyone together."
        )

    elif "graduation" in event_name:
        return (
            "A special celebration of academic achievements "
            "and hard work. Join family and friends to mark "
            "this important milestone."
        )

    else:
        return (
            "A special event bringing people together "
            "for a memorable and enjoyable experience. "
            "Join us to celebrate and create wonderful memories."
        )


# --------------------------------------------------
# SIGNUP
# --------------------------------------------------

def signup(request):

    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    else:

        form = SignUpForm()

    return render(
        request,
        "registration/signup.html",
        {
            "form": form,
        },
    )


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

@login_required
def dashboard(request):

    today = timezone.localdate()

    events = Event.objects.filter(
        created_by=request.user,
        date__gte=today,
    ).order_by("date")

    for event in events:

        done, total = event.progress()

        event.done_count = done
        event.total_count = total

        first_task = (
            event.tasks
            .filter(
                deadline__gte=today,
                done=False,
            )
            .order_by("deadline")
            .first()
        )

        event.preparation_date = (
            first_task.deadline if first_task else None
        )

        days_left = (
            event.date - today
        ).days

        if days_left == 0:

            event.reminder = "Your event is today!"

        elif days_left == 1:

            event.reminder = "Your event is tomorrow!"

        elif days_left <= 3:

            event.reminder = "Your event is very close!"

        elif days_left <= 7:

            event.reminder = "Your event is coming soon!"

        elif (
            event.preparation_date
            and today == event.preparation_date
        ):

            event.reminder = "Preparation starts today!"

        elif event.preparation_date:

            event.reminder = (
                "Preparation starts on "
                f"{event.preparation_date.strftime('%d %b %Y')}."
            )

        else:

            event.reminder = (
                "No upcoming preparation tasks."
            )

    return render(
        request,
        "events/dashboard.html",
        {
            "events": events,
        },
    )


# --------------------------------------------------
# SUCCESSFUL EVENTS
# --------------------------------------------------

@login_required
def successful_events(request):

    today = timezone.localdate()

    past_events = Event.objects.filter(
        created_by=request.user,
        date__lt=today,
    ).order_by("-date")

    completed_events = []

    for event in past_events:

        done, total = event.progress()

        if total > 0 and done == total:

            event.done_count = done
            event.total_count = total

            completed_events.append(event)

    return render(
        request,
        "events/successful_events.html",
        {
            "successful_events": completed_events,
        },
    )


# --------------------------------------------------
# TEMPORARY FILE HELPER
# --------------------------------------------------

def _read_uploaded_file(uploaded_file):

    suffix = os.path.splitext(
        uploaded_file.name
    )[1].lower()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temporary_file:

        for chunk in uploaded_file.chunks():

            temporary_file.write(chunk)

        return temporary_file.name


# --------------------------------------------------
# CREATE EVENT
# --------------------------------------------------

@login_required
def event_create(request):

    if request.method == "GET":

        form = EventForm()

        return render(
            request,
            "events/event_form.html",
            {
                "form": form,
            },
        )

    form = EventForm(
        request.POST,
        request.FILES,
    )

    if not form.is_valid():

        return render(
            request,
            "events/event_form.html",
            {
                "form": form,
            },
        )

    event = form.save(commit=False)

    event.created_by = request.user

    uploaded_file = request.FILES.get("upload")

    extracted_text = ""

    # --------------------------------------------------
    # READ UPLOADED IMAGE, PDF, OR DOCX
    # --------------------------------------------------

    if uploaded_file:

        temporary_path = None

        try:

            temporary_path = _read_uploaded_file(
                uploaded_file
            )

            extracted_text = extract_text(
                temporary_path
            )

            print(
                "\n========== EXTRACTED TEXT =========="
            )

            print(extracted_text)

            print(
                "====================================\n"
            )

            # ------------------------------------------
            # EVENT TITLE
            # ------------------------------------------

            if not (event.title or "").strip():

                event.title = (
                    find_event_title(extracted_text) or ""
                )

            # ------------------------------------------
            # EVENT DATE
            # ------------------------------------------

            if not event.date:

                extracted_date = find_date(
                    extracted_text
                )

                if extracted_date:

                    if isinstance(
                        extracted_date,
                        str,
                    ):

                        event.date = parse_date(
                            extracted_date
                        )

                    else:

                        event.date = extracted_date

            # ------------------------------------------
            # EVENT TIME
            # ------------------------------------------

            if not event.time:

                extracted_time = find_time(
                    extracted_text
                )

                if extracted_time:

                    parsed_time = parse_time(
                        extracted_time
                    )

                    if parsed_time:

                        event.time = parsed_time

                    else:

                        print(
                            "Could not parse extracted time:",
                            extracted_time,
                        )

            # ------------------------------------------
            # EVENT VENUE
            # ------------------------------------------

            if not (event.venue or "").strip():

                event.venue = (
                    find_venue(extracted_text) or ""
                )

            # ------------------------------------------
            # EVENT TYPE
            # ------------------------------------------

            if not (event.event_type or "").strip():

                event.event_type = (
                    event.title or ""
                )

            # ------------------------------------------
            # EVENT DESCRIPTION
            # ------------------------------------------

            if not (event.description or "").strip():

                extracted_description = find_description(
                    extracted_text
                )

                if extracted_description:

                    event.description = (
                        extracted_description
                    )

        except Exception as error:

            print(
                f"Document extraction failed: {error}"
            )

            form.add_error(
                "upload",
                "We could not read this file. Please check "
                "the file, confirm OCR is installed, or "
                "enter the event details manually.",
            )

            return render(
                request,
                "events/event_form.html",
                {
                    "form": form,
                },
            )

        finally:

            if (
                temporary_path
                and os.path.exists(temporary_path)
            ):

                os.remove(temporary_path)

    # --------------------------------------------------
    # VALIDATE REQUIRED EVENT DETAILS
    # --------------------------------------------------

    if not (event.title or "").strip():

        form.add_error(
            "title",
            "Please enter the event title or upload "
            "a poster that clearly shows the title.",
        )

    if not event.date:

        form.add_error(
            "date",
            "Please enter the event date or upload "
            "a poster that clearly shows the date.",
        )

    if form.errors:

        return render(
            request,
            "events/event_form.html",
            {
                "form": form,
            },
        )

    # --------------------------------------------------
    # DEFAULT DESCRIPTION
    # --------------------------------------------------

    if not (event.description or "").strip():

        event.description = get_default_description(
            event.title,
            event.event_type,
        )

    # --------------------------------------------------
    # SAVE EVENT
    # --------------------------------------------------

    event.save()

    # --------------------------------------------------
    # GENERATE CHECKLIST
    # --------------------------------------------------

    extracted_tasks = find_checklist_items(
        extracted_text
    )

    today = timezone.localdate()

    if extracted_tasks:

        for task_title in extracted_tasks:

            Task.objects.create(
                event=event,
                title=task_title,
                deadline=today,
            )

    else:

        checklist = get_checklist(
            event.title,
            event.event_type,
        )

        for task_title, days_before in checklist:

            task_deadline = (
                event.date - timedelta(
                    days=days_before
                )
            )

            if task_deadline < today:

                task_deadline = today

            Task.objects.create(
                event=event,
                title=task_title,
                deadline=task_deadline,
            )

    return redirect(
        "event_detail",
        pk=event.pk,
    )


# --------------------------------------------------
# EVENT DETAILS
# --------------------------------------------------

@login_required
def event_detail(request, pk):

    event = get_object_or_404(
        Event,
        pk=pk,
        created_by=request.user,
    )

    today = timezone.localdate()

    tasks = event.tasks.all().order_by(
        "deadline",
        "id",
    )

    done, total = event.progress()

    event_completed = (
        total > 0
        and done == total
        and today >= event.date
    )

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "tasks": tasks,
            "today": today,
            "done_count": done,
            "total_count": total,
            "event_completed": event_completed,
        },
    )


# --------------------------------------------------
# ADD CUSTOM CHECKLIST TASK
# --------------------------------------------------

@login_required
@require_POST
def add_task(request, pk):

    event = get_object_or_404(
        Event,
        pk=pk,
        created_by=request.user,
    )

    task_title = request.POST.get(
        "title",
        "",
    ).strip()

    deadline_value = request.POST.get(
        "deadline",
        "",
    ).strip()

    assigned_to = request.POST.get(
        "assigned_to",
        "",
    ).strip()

    if not task_title:

        return redirect(
            "event_detail",
            pk=event.pk,
        )

    task_deadline = None

    if deadline_value:

        task_deadline = parse_date(
            deadline_value
        )

        if not task_deadline:

            return redirect(
                "event_detail",
                pk=event.pk,
            )

    Task.objects.create(
        event=event,
        title=task_title,
        deadline=task_deadline,
        assigned_to=assigned_to,
    )

    return redirect(
        "event_detail",
        pk=event.pk,
    )


# --------------------------------------------------
# TOGGLE TASK
# --------------------------------------------------

@login_required
@require_POST
def toggle_task(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        event__created_by=request.user,
    )

    task.done = not task.done

    task.save(
        update_fields=["done"]
    )

    return redirect(
        "event_detail",
        pk=task.event.pk,
    )


# --------------------------------------------------
# DELETE EVENT
# --------------------------------------------------

@login_required
@require_POST
def delete_event(request, pk):

    event = get_object_or_404(
        Event,
        pk=pk,
        created_by=request.user,
    )

    event.delete()

    return redirect("dashboard")
