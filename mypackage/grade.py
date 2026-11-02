# grade.py

def grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "Fail"
