# cleaning.py

import string

def clean(text):

    for ch in string.punctuation:
        text = text.replace(ch, "")

    text = " ".join(text.split())

    return text
