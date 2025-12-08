# Given the test scores of 10 students in Physics and History, compute Karl Pearson’s coefficient of correlation between these scores.
# Round the result to three decimal places.

# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15

# Pearson's Correlation Coefficient

# Where: -  is Pearson's correlation coefficient,
# -  and  are the individual sample points,
# -  and  are the means of the  and  values,
# -  is the number of data points.

# Output Format

# Print the correlation coefficient as a floating-point value rounded to three decimal places, without leading or trailing spaces.

# For example, if your answer is 0.255. In python you can print using

# print("0.255")
# This is NOT the actual answer - just the format in which you should provide your answer.

# If you would like to test code that calculates the value, choose 'Test agains custom input' and enter anything into the input box, e.g., 'x'.
# The code will not run without some value in the input box. When you are satisfied with the output, press 'Submit Code'.


# INPUT LIST
x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)

a = [i - x_mean for i in x]
b = [j - y_mean for j in y]

num = sum([x * y for x, y in zip(a, b)])
den = (sum([a[k]**2 for k in range(len(a))])*sum([b[k]**2 for k in range(len(b))]))**(1/2)

r= num/den

print("%.3f" %(r))