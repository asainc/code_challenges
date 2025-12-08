# The number of calls coming per minute into a hotels reservation center is Poisson random variable with mean 3.

# (a) Find the probability that no calls come in a given 1 minute period.

# (b) Assume that the number of calls arriving in two different minutes are independent. Find the probability that atleast two calls will arrive in a given two minute period.

# Submission Modes and Output Format

# You may submit either an R or Python program to accomplish the above task, or solve the problem on pen-and-paper. Your output should be two floating point/decimal numbers(as answers to 1st and 2nd questions respectively), correct to 3 places of decimal.

# In the text box below, enter two floating point/decimal numbers(as answers to 1st and 2nd questions respectively), correct to 3 places of decimal.

# Alternatively, you may submit an R program, which uses the above parameters (hard-coded) and computes the answer.

# Your answer should resemble something like:

# 9.123
# 8.345

import math

# Média por minuto
lam = 3

# (a) Probabilidade de zero chamadas em 1 minuto
p_zero = math.exp(-lam) * (lam**0) / math.factorial(0)

# (b) Probabilidade de pelo menos duas chamadas em 2 minutos
# Em 2 minutos, a média dobra
lam2 = 2 * lam

# P(at least 2) = 1 - [P(0) + P(1)]
p0 = math.exp(-lam2) * (lam2**0) / math.factorial(0)
p1 = math.exp(-lam2) * (lam2**1) / math.factorial(1)
p_at_least_2 = 1 - (p0 + p1)

print(f"{p_zero:.3f}")
print(f"{p_at_least_2:.3f}")
