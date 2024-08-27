# -*- coding: utf-8 -*-
"""Lab_2_Exercise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1anTi_MN4JNM_BQJsdOqcFkgBebRE5VjM

Question 1 in Lab 2 Exercise
"""

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array.shape)

arr1 = np.random.random(20)
print('Array with random values')
# Variance :  represents the dispersion or spread of a set of data points around their mean (average).
sample_variance = np.var(arr1, ddof=1)
print(f'Sample Variance {sample_variance}')
print(f'Variance with random values : {np.var(arr1)}')

print(f'Mean with random values : {np.mean(arr1)}')

# for variance
print('Array with Specified values')
print(f'Sample Variance {np.var(array, ddof=1)}')
print(f'Variance : {np.var(array)}')
print(f'Mean : {np.mean(array)}')

"""Question 2 in Lab 2 Exercise"""

x = np.random.random(8)
y = np.random.random(8)

print(x)
print(y)

cov_mat = np.stack((x, y), axis=0)
# Here we take two, one dimensional array so we have to combine both the arrays for that we using the stack() function
print('\nCoavriance of a matrix : (x,y)\n')
print(np.cov(cov_mat))

print(f'\nShape of covariance matrix is {np.shape(cov_mat)}')

randArr = np.random.random((3,3))
# Here we initiallly creating a 3X3 matrix so we can directly calculate the covariance of the matrix by passing it to the cov() function
#Co-variance:   indicates the extent to which two variables change together.
print(np.cov(randArr))
print(f'\nShape of covariance matrix is {np.shape(randArr)}')

"""Question 3 in Lab 2 Exercise"""

# For Corelation
# np.correlate() is designed to work with 1D arrays, and when you pass it a 2D array, it doesn't know how to compute the correlation properly.
arr1 = np.random.random(10)
arr2 = np.random.random(10)
#Corelation :  describes the extent to which two variables move in relation to each other
print(arr1)
print(arr2)
print(np.correlate(arr1, arr2))

"""Question 4 in Lab 2 Exercise"""

# Generate a random MxN matrix
feature_matrix = np.random.random((5, 10))
print("Feature Matrix (MxN):")
print(feature_matrix)

# Compute the Covariance Matrix
covariance_matrix = np.cov(feature_matrix)
print("\nCovariance Matrix (MxM):")
print(covariance_matrix)

# Compute the Correlation Matrix
correlation_matrix = np.corrcoef(feature_matrix)
print("\nCorrelation Matrix (MxM):")
print(correlation_matrix)