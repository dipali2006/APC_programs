import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85]

plt.hist(marks, bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()