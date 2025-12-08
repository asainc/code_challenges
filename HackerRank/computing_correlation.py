import sys
import math

data = sys.stdin.read().strip().split()
N = int(data[0])
vals = list(map(int, data[1:]))

# Initialize sums
sumM = sumP = sumC = 0
sumM2 = sumP2 = sumC2 = 0
sumMP = sumPC = sumCM = 0

idx = 0
for _ in range(N):
    M = vals[idx]; P = vals[idx+1]; C = vals[idx+2]
    idx += 3

    sumM += M
    sumP += P
    sumC += C

    sumM2 += M*M
    sumP2 += P*P
    sumC2 += C*C

    sumMP += M*P
    sumPC += P*C
    sumCM += C*M

def corr(sumX, sumY, sumXY, sumX2, sumY2):
    num = N * sumXY - sumX * sumY
    den = math.sqrt((N * sumX2 - sumX*sumX) * (N * sumY2 - sumY*sumY))
    return num / den

# Compute correlations
r_MP = corr(sumM, sumP, sumMP, sumM2, sumP2)
r_PC = corr(sumP, sumC, sumPC, sumP2, sumC2)
r_CM = corr(sumC, sumM, sumCM, sumC2, sumM2)

# Print with exactly two decimal places
print(f"{r_MP:.2f}")
print(f"{r_PC:.2f}")
print(f"{r_CM:.2f}")
