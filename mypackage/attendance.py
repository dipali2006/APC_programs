# attendance.py

def eligible(attended, total):
    per = (attended / total) * 100

    if per >= 75:
        return "Eligible"
    else:
        return "Not Eligible"
