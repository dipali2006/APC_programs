import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")

plt.subplot(2, 2, 4)
plt.pie(y, labels=x)
plt.title("Pie Chart")

plt.tight_layout()
plt.show()