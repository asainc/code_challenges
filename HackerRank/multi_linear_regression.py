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
