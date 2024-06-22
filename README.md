# EGIER Warehouse Capacity Analysis
This repository contains the solutions to the EGIER warehouse capacity analysis problems. The analysis includes:

1. Finding the Production Trend (Problem 1):
- Fitting a polynomial regression model to the monthly production data to identify the trend.
- Avoiding a linear approach by using a polynomial of degree 3 for better accuracy.
  
2. Converting the Mathematical Model to Numerical Form (Problem 2):
- Converting the polynomial model from Problem 1 into its numerical form using the Taylor Series.
- Providing an explanation about the accuracy of the conversion.

3. Predicting When to Build a New Warehouse (Problem 3):
- Using the polynomial trend to predict when production will exceed the current warehouse capacity of 25,000 bags.
- Determining the month when the construction of a new warehouse should start, accounting for a 13-month lead time.
