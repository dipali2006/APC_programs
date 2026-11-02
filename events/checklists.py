
# events/checklists.py

# Each task is written as:
# ("Task description", days_before_event)


TEMPLATES = {

    # BIRTHDAY CELEBRATION
    "birthday": [
        ("Prepare guest list and send invitations", 7),
        ("Order birthday cake", 3),
        ("Arrange balloons and decorations", 2),
        ("Organize food, snacks and drinks", 2),
        ("Prepare music, games and party activities", 1),
    ],

    "birthday party": [
        ("Prepare guest list and send invitations", 7),
        ("Order birthday cake", 3),
        ("Arrange balloons and decorations", 2),
        ("Organize food, snacks and drinks", 2),
        ("Prepare music, games and party activities", 1),
    ],

    # INDEPENDENCE DAY
    "independence day": [
        ("Get approval and finalize celebration schedule", 14),
        ("Invite chief guest", 10),
        ("Arrange flag, flagpole and decorations", 5),
        ("Rehearse march past and national anthem", 3),
        ("Arrange sound system and refreshments", 1),
    ],

    # REPUBLIC DAY
    "republic day": [
        ("Get approval and finalize celebration plan", 14),
        ("Invite chief guest", 10),
        ("Arrange flag and flagpole", 5),
        ("Practice parade and cultural program", 4),
        ("Arrange sound system and refreshments", 1),
    ],

    # ANNUAL DAY
    "annual day": [
        ("Book auditorium and finalize schedule", 30),
        ("Finalize performances and participants", 20),
        ("Invite chief guest and print invitations", 15),
        ("Arrange lights, sound and decorations", 7),
        ("Prepare prizes and conduct final rehearsal", 2),
    ],

    # SPORTS DAY
    "sports day": [
        ("Book sports ground and prepare schedule", 21),
        ("Form teams and confirm participants", 14),
        ("Prepare sports equipment and track", 10),
        ("Arrange first aid, referees and volunteers", 5),
        ("Prepare medals and certificates", 2),
    ],

    # FRESHERS PARTY
    "freshers party": [
        ("Get college approval and book venue", 21),
        ("Finalize party theme and schedule", 14),
        ("Arrange decorations, sound and lights", 7),
        ("Finalize performances and activities", 3),
        ("Conduct final rehearsal and venue check", 1),
    ],

    # FAREWELL
    "farewell": [
        ("Get approval and book venue", 21),
        ("Prepare invitations and guest list", 14),
        ("Collect farewell messages and memories", 7),
        ("Arrange decorations, food and refreshments", 3),
        ("Complete final venue preparation", 1),
    ],

    # HACKATHON
    "hackathon": [
        ("Get approval and finalize hackathon theme", 30),
        ("Arrange mentors, judges and registration", 21),
        ("Prepare problem statements", 14),
        ("Arrange internet, power backup and equipment", 5),
        ("Test venue and finalize participant arrangements", 2),
    ],

    # SEMINAR
    "seminar": [
        ("Get approval and invite speaker", 14),
        ("Book seminar hall and finalize schedule", 10),
        ("Prepare presentation and seminar materials", 5),
        ("Arrange projector and sound system", 2),
        ("Confirm speaker and final arrangements", 1),
    ],

    # WORKSHOP
    "workshop": [
        ("Get approval and finalize trainer", 21),
        ("Book laboratory or workshop venue", 14),
        ("Prepare workshop materials", 7),
        ("Register participants and arrange equipment", 5),
        ("Test equipment and finalize setup", 2),
    ],

    # BLOOD DONATION CAMP
    "blood donation camp": [
        ("Get approval and contact blood bank", 21),
        ("Arrange medical team and equipment", 14),
        ("Prepare donor registration forms", 7),
        ("Arrange volunteers and seating", 3),
        ("Arrange water and refreshments", 1),
    ],

    # CULTURAL FEST
    "cultural fest": [
        ("Get approval and book venue", 30),
        ("Finalize cultural programs and participants", 21),
        ("Arrange decorations and invitations", 14),
        ("Arrange sound, lights and equipment", 7),
        ("Conduct final rehearsal", 2),
    ],

    # SCIENCE EXHIBITION
    "science exhibition": [
        ("Get approval and select exhibition topics", 21),
        ("Register participating students", 14),
        ("Prepare models and projects", 10),
        ("Arrange tables, posters and labels", 5),
        ("Complete final exhibition setup", 1),
    ],

    # NAVRATRI
    "navratri": [
        ("Get approval and form organizing team", 21),
        ("Finalize Navratri celebration plan", 14),
        ("Arrange venue and decorations", 7),
        ("Arrange music, sound system and activities", 5),
        ("Complete final venue and decoration check", 1),
    ],

    # DUSSEHRA
    "dussehra": [
        ("Finalize celebration plan and venue", 14),
        ("Arrange decorations and required materials", 10),
        ("Organize cultural activities", 7),
        ("Arrange sound system and volunteers", 3),
        ("Complete final preparations", 1),
    ],

    # DIWALI
    "diwali": [
        ("Finalize Diwali celebration plan", 14),
        ("Arrange decorations and lighting", 10),
        ("Plan cultural activities", 7),
        ("Arrange refreshments and materials", 3),
        ("Complete final venue check", 1),
    ],

    # WEDDING
    "wedding": [
        ("Prepare guest list and send invitations", 30),
        ("Book venue and confirm decorations", 20),
        ("Arrange catering and finalize menu", 15),
        ("Confirm outfits and accessories", 7),
        ("Complete final arrangements with vendors", 2),
    ],

    # ENGAGEMENT
    "engagement": [
        ("Prepare guest list and send invitations", 14),
        ("Book venue and arrange decorations", 10),
        ("Order cake and finalize menu", 7),
        ("Arrange outfits and photography", 3),
        ("Complete final venue preparation", 1),
    ],

    # PICNIC
    "picnic": [
        ("Choose destination and prepare itinerary", 7),
        ("Arrange transport and confirm participants", 5),
        ("Plan food, snacks and water", 3),
        ("Pack games and picnic essentials", 1),
        ("Check weather and travel arrangements", 1),
    ],

    # TRIP / TOUR
    "trip": [
        ("Choose destination and finalize itinerary", 7),
        ("Book transport and accommodation", 5),
        ("Confirm participants and travel details", 3),
        ("Pack clothes and travel essentials", 1),
        ("Check weather and tickets", 1),
    ],

    # MEETING
    "meeting": [
        ("Prepare meeting agenda", 3),
        ("Send invitations to participants", 2),
        ("Book meeting room or online meeting link", 1),
        ("Prepare documents and presentation", 1),
        ("Confirm attendance and equipment", 0),
    ],

    # BABY SHOWER
    "baby shower": [
        ("Prepare guest list and send invitations", 7),
        ("Arrange decorations and theme", 5),
        ("Plan food and refreshments", 3),
        ("Prepare games and activities", 2),
        ("Complete final venue preparation", 1),
    ],

    # HOUSEWARMING
    "housewarming": [
        ("Prepare guest list and send invitations", 7),
        ("Arrange home decorations and seating", 5),
        ("Plan food and refreshments", 3),
        ("Prepare पूजा or housewarming arrangements", 2),
        ("Complete final home preparation", 1),
    ],

    # DEFAULT FOR OTHER EVENTS
    "default": [
        ("Finalize event plan and schedule", 7),
        ("Prepare guest list and send invitations", 5),
        ("Arrange venue and decorations", 3),
        ("Organize food and required materials", 2),
        ("Complete final event preparations", 1),
    ],
}


def get_checklist(event_name, event_type=""):
    """
    Select a suitable checklist using the event title and event type.

    The function checks:
    1. Exact event title
    2. Exact event type
    3. Matching keywords
    4. Default checklist
    """

    event_name = (event_name or "").strip().lower()
    event_type = (event_type or "").strip().lower()

    combined_text = f"{event_name} {event_type}"

    # Exact matching
    if event_name in TEMPLATES:
        return TEMPLATES[event_name]

    if event_type in TEMPLATES:
        return TEMPLATES[event_type]

    # Keyword matching
    keyword_mapping = [
        ("birthday", "birthday"),
        ("bday", "birthday"),
        ("birth day", "birthday"),
        ("independence day", "independence day"),
        ("republic day", "republic day"),
        ("annual day", "annual day"),
        ("sports day", "sports day"),
        ("sports", "sports day"),
        ("freshers", "freshers party"),
        ("farewell", "farewell"),
        ("hackathon", "hackathon"),
        ("seminar", "seminar"),
        ("workshop", "workshop"),
        ("blood donation", "blood donation camp"),
        ("cultural fest", "cultural fest"),
        ("science exhibition", "science exhibition"),
        ("exhibition", "science exhibition"),
        ("navratri", "navratri"),
        ("dussehra", "dussehra"),
        ("diwali", "diwali"),
        ("wedding", "wedding"),
        ("marriage", "wedding"),
        ("engagement", "engagement"),
        ("picnic", "picnic"),
        ("outing", "picnic"),
        ("trip", "trip"),
        ("tour", "trip"),
        ("meeting", "meeting"),
        ("baby shower", "baby shower"),
        ("housewarming", "housewarming"),
    ]

    for keyword, template_name in keyword_mapping:
        if keyword in combined_text:
            return TEMPLATES[template_name]

    return TEMPLATES["default"]
