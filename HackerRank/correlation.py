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