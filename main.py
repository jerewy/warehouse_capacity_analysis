import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Load the data from the provided URL
url = "https://stbm7resourcesprod.blob.core.windows.net:443/assessment/Assessment/afcc3c44-bc8d-41fd-bbfd-5b68530612e8.xlsx?sv=2023-08-03&se=2024-06-22T17%3A22%3A39Z&sr=b&sp=r&sig=k%2FOs2SuBogOdAydlX5jQEzDjkFsvv567zFvE6CsgBIc%3D"
data = pd.read_excel(url)

# Transpose the data for easier processing
data_transposed = data.transpose()
data_transposed.columns = ['Production']
data_transposed['Month'] = np.arange(1, 145)

# Problem 1: Polynomial regression of degree 3 using numpy polyfit
x = data_transposed['Month']
y = data_transposed['Production']
coefficients = np.polyfit(x, y, 3)

# Generate fitted values using the polynomial coefficients
x_fit = np.linspace(1, 144, 144)
y_fit = np.polyval(coefficients, x_fit)

# Plot the polynomial regression
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_fit, y_fit, '-', label='Polynomial Fit (Degree 3)')
plt.xlabel('Month')
plt.ylabel('Production')
plt.title('Polynomial Regression of Monthly Production')
plt.legend()
plt.grid(True)
plt.show()

# Problem 2: Taylor Series Conversion Explanation
# The polynomial function P(x) = c0 + c1*x + c2*x^2 + c3*x^3 is already in numerical form
# The Taylor Series expansion at x = 0 is the polynomial itself for this problem

# Coefficients of the polynomial (these are also the Taylor Series coefficients)
c0, c1, c2, c3 = coefficients

# Ensure the Taylor Series is calculated correctly
# P(x) = c0 + c1*x + c2*x**2 + c3*x**3
P_taylor = np.polyval(coefficients, x)

# Plot the Taylor Series approximation (should match the polynomial fit)
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x, P_taylor, '-', label='Taylor Series Approximation')
plt.xlabel('Month')
plt.ylabel('Production')
plt.title('Taylor Series Approximation of Monthly Production')
plt.legend()
plt.grid(True)
plt.show()

# Explanation of accuracy
# Since the polynomial model is already in the form of a Taylor Series around x = 0,
# the conversion is exact and does not introduce any approximation error.

# Problem 3: Find the month when production will exceed warehouse capacity (25,000 bags)
# Define the polynomial function
def polynomial(month):
    return np.polyval(coefficients, month)

# Define the function to find the root of
def func_to_solve(month):
    return polynomial(month) - 25000

# Initial guess for the root
initial_guess = 144

# Find the root
month_exceed = fsolve(func_to_solve, initial_guess)[0]

# Calculate the month to start building the new warehouse
month_to_start_building = month_exceed - 13

# Ensure the month to start building is an integer and valid month
month_to_start_building = max(1, int(np.ceil(month_to_start_building)))

print(f"Month to start building the new warehouse: {month_to_start_building}")

# Plot the polynomial regression and the 25,000 threshold line
x_fit = np.linspace(1, 200, 200)
y_fit = np.polyval(coefficients, x_fit)

plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_fit, y_fit, '-', label='Polynomial Fit (Degree 3)')
plt.axhline(y=25000, color='r', linestyle='--', label='Warehouse Capacity (25,000)')
plt.axvline(x=month_exceed, color='g', linestyle='--', label='Exceed Month')
plt.xlabel('Month')
plt.ylabel('Production')
plt.title('Prediction of When to Start Building New Warehouse')
plt.legend()
plt.grid(True)
plt.show()
