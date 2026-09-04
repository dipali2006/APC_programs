# frequency.py

def frequency(text):

    d = {}

    words = text.split()

    for word in words:

        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d
