import matplotlib.pyplot as plt

sizes = [40, 30, 20, 10]
labels = ["Python", "Java", "C++", "Other"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()
