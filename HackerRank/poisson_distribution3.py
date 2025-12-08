import math

lam = 3

p_zero = math.exp(-lam) * (lam**0) / math.factorial(0)

lam2 = 2 * lam

p0 = math.exp(-lam2) * (lam2**0) / math.factorial(0)
p1 = math.exp(-lam2) * (lam2**1) / math.factorial(1)
p_at_least_2 = 1 - (p0 + p1)

print(f"{p_zero:.3f}")
print(f"{p_at_least_2:.3f}")
