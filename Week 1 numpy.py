# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating an array of even integers from 30 to 70 (inclusive) with a step size of 2 using np.arange()
array = np.arange(30, 71, 2)

# Printing a message indicating an array of all the even integers from 30 to 70
print("Array of all the even integers from 30 to 70")

# Printing the array of all the even integers from 30 to 70
print(array) 

# Generating an array of 15 random numbers from a standard normal distribution using np.random.normal()
rand_num = np.random.normal(0, 1, 15)

# Printing a message indicating 15 random numbers from a standard normal distribution
print("15 random numbers from a standard normal distribution:")

# Printing the array of 15 random numbers
print("The random variable of 15 numbers is:" ,rand_num) 

# declare vectors
x = [1, 2]
y = [3, 4]
 
# find cross product of
# two given vectors
result = np.cross(x, y)
 
# show the result
print("cross product of the given vectors is", result)

# create a 3x3 matrix
matrix = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# calculate the determinant of the matrix
determinant = np.linalg.det(matrix)
print("determinent is:" ,determinant)

# Generating a 3x3x3 NumPy array 'x' filled with random floats between 0 and 1 using np.random.random()

x = np.random.random((3, 3, 3))

# Printing the array 'x'
print(x) 

# Generating a 5x5 NumPy array 'x' filled with random floats between 0 and 1 using np.random.random()

x = np.random.random((5, 5))

# Printing the original array 'x'
print("Original Array:")
print(x)

# Calculating the minimum and maximum values in array 'x' using x.min() and x.max() functions
xmin, xmax = x.min(), x.max()

# Printing the minimum and maximum values of the array 'x'
print("Minimum and Maximum Values:")
print(xmin, xmax) 

# Creating an array 'x' using arange with 6 elements
x = np.arange(6)

# Displaying the original array 'x'
print("\nOriginal array:")
print(x)

# Calculating the mean of the array 'x' using np.mean()
r1 = np.mean(x)

# Calculating the average of the array 'x' using np.average()
r2 = np.average(x)

# Asserting if the results from np.mean() and np.average() are close
assert np.allclose(r1, r2)

# Displaying the calculated mean of the array 'x'
print("\nMean: ", r1)

# Calculating the standard deviation of the array 'x' using np.std()
r1 = np.std(x)

# Calculating the standard deviation manually
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2))

# Asserting if the results from np.std() and manual calculation are close
assert np.allclose(r1, r2)

# Displaying the calculated standard deviation of the array 'x'
print("\nstd: ", r1)

# Calculating the variance of the array 'x' using np.var()
r1 = np.var(x)

# Calculating the variance manually
r2 = np.mean((x - np.mean(x)) ** 2)

# Asserting if the results from np.var() and manual calculation are close
assert np.allclose(r1, r2)

# Displaying the calculated variance of the array 'x'
print("\nvariance: ", r1) 
