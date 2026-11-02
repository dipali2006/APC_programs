
import os

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Event


class EventForm(forms.ModelForm):

    upload = forms.FileField(
        required=False,
        label="Upload Event Poster (Image, PDF, or DOCX)",
        help_text="Supported formats: JPG, JPEG, PNG, BMP, PDF, DOCX",
    )

    class Meta:
        model = Event

        fields = [
            "title",
            "event_type",
            "date",
            "time",
            "venue",
            "description",
            "upload",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter event name",
                }
            ),

            "event_type": forms.TextInput(
                attrs={
                    "placeholder": "Example: Wedding, Birthday, Workshop",
                }
            ),

            "date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "time": forms.TimeInput(
                attrs={
                    "type": "time",
                }
            ),

            "venue": forms.TextInput(
                attrs={
                    "placeholder": "Enter event venue",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Enter your event description...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # These fields can be filled automatically from the uploaded poster.
        self.fields["title"].required = False
        self.fields["date"].required = False
        self.fields["time"].required = False
        self.fields["venue"].required = False
        self.fields["event_type"].required = False
        self.fields["description"].required = False

    def clean_upload(self):
        uploaded_file = self.cleaned_data.get("upload")

        if uploaded_file:
            allowed_extensions = [
                ".jpg",
                ".jpeg",
                ".png",
                ".bmp",
                ".pdf",
                ".docx",
            ]

            extension = os.path.splitext(
                uploaded_file.name
            )[1].lower()

            if extension not in allowed_extensions:
                raise forms.ValidationError(
                    "Upload a JPG, JPEG, PNG, BMP, PDF, or DOCX file."
                )

            if uploaded_file.size > 10 * 1024 * 1024:
                raise forms.ValidationError(
                    "File size must be less than 10 MB."
                )

        return uploaded_file

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        date = cleaned_data.get("date")
        uploaded_file = cleaned_data.get("upload")

        # Manual event creation requires title and date.
        # When a poster is uploaded, OCR may provide these details.
        if not uploaded_file:
            if not title:
                self.add_error(
                    "title",
                    "Please enter the event title.",
                )

            if not date:
                self.add_error(
                    "date",
                    "Please enter the event date.",
                )

        return cleaned_data


class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label="Email",
    )

    class Meta:
        model = User

        fields = [
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"].lower().strip()

        if User.objects.filter(username=email).exists():
            raise forms.ValidationError(
                "This email is already registered. "
                "Please login or use another email."
            )

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email is already registered. "
                "Please login or use another email."
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        email = self.cleaned_data["email"]

        user.username = email
        user.email = email

        if commit:
            user.save()

        return user
