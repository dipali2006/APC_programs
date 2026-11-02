import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y, label="Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.grid(True)
plt.legend()
plt.show()