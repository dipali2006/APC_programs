import matplotlib.pyplot as plt

x = ["Python", "Java", "C++"]
y = [80, 65, 70]

plt.barh(x, y)
plt.title("Horizontal Bar Chart")
plt.show()