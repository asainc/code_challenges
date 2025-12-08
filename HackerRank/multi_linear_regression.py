# Objective
# In this challenge, we practice using multiple linear regression to predict housing prices. Check out the Resources tab for helpful videos!

# Task

# Charlie is looking to buy a house and has collected data on desirable features in the area.
# For each house, he recorded feature values on a scale from  to , along with the price per square foot for some houses.
# However, some of the houses lack pricing data.
# You need to estimate the price per square foot for these houses based on the available feature data and the pricing information for the other houses.

# The data is structured such that:

# There are  features for each house.
# Each row contains  feature values followed by the price per square foot (totaling  columns).
# Charlie has observed data for  houses, resulting in a table with  rows and  columns.
# The price per square foot is approximately linearly related to the features. Your task is to predict the missing prices using a regression-based technique.

# Hints
# - Focus on using regression to model the relationship between the features and the price per square foot.
# You don't need to address bias-variance trade-offs at this stage.

# Input Format

# The first line contains  space-separated integers,  (the number of observed features) and  (the number of rows/houses for which Charlie has noted both the features and price per square foot).
# The  subsequent lines each contain  space-separated floating-point numbers describing a row in the table;  first  elements are the noted features for a house, and the very last element is its price per square foot.

# The next line (following the table) contains a single integer, , denoting the number of houses for for which Charlie noted features but does not know the price per square foot.
# The  subsequent lines each contain  space-separated floating-point numbers describing the features of a house for which pricing is not known.

# Constraints
# 10 <= F <= 10
# 5 <= N <= 100
# 1 <= T <= 100
# 0 <= Price Per Square Foot <= 10**6
# 0 <= Factor Values <= 1



# Scoring

# For each test case, we will compute the following:


# There are multiple ways to approach this problem that account for bias, variance, various subjective factors, and "noise". We take a realistic approach to scoring and permit up to a  swing of our expected answer.

# , where  is the maximum possible score for the test case.
# Consider a test case in which we only need to find the pricing for  house. Suppose our expected answer is , and your answer is :



# The score for a test case with  points 

# Output Format

# Print  lines, where each line  contains the predicted price for the  house (from the second table of houses with unknown prices per square foot).

# Sample Input

# STDIN                  Function
# -----                  --------
# 2 7                     F = 2, N = 7
# 0.18 0.89 109.85    Features = [0.18, 0.89] Square foot cost = 109.85
# 1.0 0.26 155.72
# 0.92 0.11 137.66
# 0.07 0.37 76.17
# 0.85 0.16 139.75
# 0.99 0.41 162.6
# 0.87 0.47 151.77
# 4                       T = 4
# 0.49 0.18             Features for the first property
# 0.57 0.8
# 0.56 0.64
# 0.76 0.18
# Sample Output

# 105.22
# 142.68
# 132.94
# 129.71






import numpy as np

# Read F and N
F, N = map(int, input().split())

# Read training data
X = []
y = []
for _ in range(N):
    row = list(map(float, input().split()))
    X.append([1.0] + row[:F])  # add bias term
    y.append(row[F])

X = np.array(X)
y = np.array(y)

# Compute parameters using the normal equation
beta = np.linalg.inv(X.T @ X) @ X.T @ y

# Read T (number of missing-price houses)
T = int(input())

# Predict for each of the T houses
for _ in range(T):
    features = list(map(float, input().split()))
    x_new = np.array([1.0] + features)
    y_pred = x_new @ beta
    print(y_pred)
