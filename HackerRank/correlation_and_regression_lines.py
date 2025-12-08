x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

x_hat = sum(x)/len(x)
y_hat = sum(y)/len(y)

a = [i - x_hat for i in x]
b = [j - y_hat for j in y]

m = sum([a[i]*b[i] for i in range (len(a))])/sum([a[i]**2 for i in range(len(a))])

print('%.3f'%(m))