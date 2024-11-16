import math

def sum_50(x, n):
    S = x
    for i in range(1, n+1):
        S += (x**(2*i + 1)) / math.factorial(2*i + 1)
    return S