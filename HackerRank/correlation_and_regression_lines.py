# Given the test scores of 10 students in Physics and History, compute the slope of the regression line obtained by treating Physics as the independent variable. The result should be rounded to three decimal places.

# The scores to use:

# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15
# Slope of a regression line

# Where:

#  is the slope of the regression line,
#  and  are the data points,
#  and  are the means of the -values and -values, respectively,
#  is the number of data points.
# Output Format

# In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like: 0.255

# This is NOT the actual answer - just the format in which you should provide your answer.

x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

x_hat = sum(x)/len(x)
y_hat = sum(y)/len(y)

a = [i - x_hat for i in x]
b = [j - y_hat for j in y]

m = sum([a[i]*b[i] for i in range (len(a))])/sum([a[i]**2 for i in range(len(a))])

print('%.3f'%(m))