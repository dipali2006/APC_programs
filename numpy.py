
# 1. Write a Python program using NumPy to create a one-dimensional
# array containing 10 integers and display its size, data type,
# and number of dimensions.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)



# 2. Create two NumPy arrays of 5 integers each.
# Perform addition, subtraction, multiplication, division, and modulus.

import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Array 1:", a)
print("Array 2:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# 3. Create a NumPy array containing 10 numbers.
# Find and display the maximum, minimum, sum, and average.

import numpy as np

arr = np.array([12, 25, 34, 45, 56, 67, 78, 89, 90, 100])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))



# 4. Create a NumPy array of integers from 1 to 20.
# Use Boolean indexing to display even and odd numbers.

import numpy as np

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


# 5. Create a one-dimensional array containing numbers from 1 to 12.
# Reshape it into 2x6, 3x4, and 4x3 matrices.

import numpy as np

arr = np.arange(1, 13)

print("Original Array:", arr)

print("2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("4 x 3 Matrix:")
print(arr.reshape(4, 3))


# 6. Create two 3x3 NumPy matrices and perform matrix addition.

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Addition:")
print(a + b)


# 7. Create two compatible matrices using NumPy
# and perform matrix multiplication using an appropriate function.

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

result = np.dot(a, b)

print("Matrix Multiplication:")
print(result)


# 8. Create a 3x4 matrix and display its transpose.

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original Matrix:")
print(arr)

print("Transpose:")
print(arr.T)


# 9. Create a 4x4 NumPy array and display the first row,
# last column, diagonal elements, and second and third rows.

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Original Matrix:")
print(arr)

print("First Row:", arr[0])
print("Last Column:", arr[:, -1])
print("Diagonal Elements:", np.diag(arr))
print("Second and Third Rows:")
print(arr[1:3])


# 10. Create a 4x4 matrix and calculate the sum
# of each row and each column separately.

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Matrix:")
print(arr)

print("Sum of Each Row:", np.sum(arr, axis=1))
print("Sum of Each Column:", np.sum(arr, axis=0))



# 11. Create a NumPy array containing numbers from 1 to 20.
# Using slicing, display the first 5 elements, last 5 elements,
# alternate elements, and elements in reverse order.

import numpy as np

arr = np.arange(1, 21)

print("Original Array:", arr)
print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse Order:", arr[::-1])


# 12. Create an array of 10 integers.
# Replace all elements greater than 50 with 0 using Boolean indexing.

import numpy as np

arr = np.array([10, 25, 60, 45, 75, 30, 90, 50, 65, 20])

print("Original Array:", arr)

arr[arr > 50] = 0

print("Modified Array:", arr)



# 13. Create an unsorted NumPy array and display it
# in ascending and descending order.

import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56, 34])

print("Original Array:", arr)
print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])


# 14. Create an array containing duplicate values.
# Find and display only the unique elements.

import numpy as np

arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60, 10])

print("Original Array:", arr)
print("Unique Elements:", np.unique(arr))


# 15. Create two NumPy arrays and concatenate them
# horizontally and vertically.

import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Array A:")
print(a)

print("Array B:")
print(b)

print("Horizontal Concatenation:")
print(np.hstack((a, b)))

print("Vertical Concatenation:")
print(np.vstack((a, b)))


# 16. Store marks of 10 students in a NumPy array.
# Calculate highest marks, lowest marks, average marks,
# median, and standard deviation.

import numpy as np

marks = np.array([78, 85, 90, 65, 72, 88, 95, 60, 80, 87])

print("Students' Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))



# 17. Take marks of 20 students, calculate the class average,
# and display the marks of students who scored above the average.

import numpy as np

marks = np.array([
    65, 78, 82, 90, 55,
    72, 88, 95, 60, 76,
    84, 69, 91, 58, 80,
    73, 86, 67, 93, 75
])

average = np.mean(marks)

print("Students' Marks:", marks)
print("Class Average:", average)
print("Marks Above Average:", marks[marks > average])


# 18. Create a 3D array of shape (2, 3, 4)
# containing numbers from 1 to 24.
# Display the array, dimensions, shape, and size.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# 19. Create a 3D array of shape (2, 3, 4).
# Access the first element, last element,
# element at index [0,1,2], and element at index [1,2,3].

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


# 20. Create a (2, 3, 4) array and calculate:
# sum of all elements, sum of each layer,
# sum along rows, and sum along columns.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=2))
print("Sum Along Columns:", np.sum(arr, axis=1))


# 21. Create a 3D array of random integers between 1 and 100.
# Replace all values greater than 50 with 0.

import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:")
print(arr)

arr[arr > 50] = 0

print("Modified 3D Array:")
print(arr)


# 22. Generate a random 3D array of shape (3, 4, 5).
# Calculate its mean, median, standard deviation,
# variance, minimum, and maximum.

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Random 3D Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))



# 23. Create a 3D NumPy array of shape (2, 3, 4)
# containing numbers from 1 to 24.
# Flatten the array and display both arrays.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D Array:")
print(arr)

flat_arr = arr.flatten()

print("Flattened 1D Array:")
print(flat_arr)



# 24. Create a 3D array containing integers from 1 to 27.
# Flatten the array and calculate its sum, average,
# maximum, and minimum.

import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)

print("Original 3D Array:")
print(arr)

flat_arr = arr.flatten()

print("Flattened Array:")
print(flat_arr)

print("Sum:", np.sum(flat_arr))
print("Average:", np.mean(flat_arr))
print("Maximum:", np.max(flat_arr))
print("Minimum:", np.min(flat_arr))



# 25. Create a random 3D NumPy array of shape (3, 4, 5).
# Flatten it and display elements greater than 50,
# even numbers, and elements less than the average value.

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Original 3D Array:")
print(arr)

flat_arr = arr.flatten()

print("Flattened Array:")
print(flat_arr)

print("Elements Greater Than 50:")
print(flat_arr[flat_arr > 50])

print("Even Numbers:")
print(flat_arr[flat_arr % 2 == 0])

average = np.mean(flat_arr)

print("Average:", average)
print("Elements Less Than Average:")
print(flat_arr[flat_arr < average])
