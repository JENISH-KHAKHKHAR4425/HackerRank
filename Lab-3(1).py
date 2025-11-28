#Naive Approach
def power_naive(b, e):
    result = 1
    for _ in range(abs(e)):  
        result *= b
    return result if e >= 0 else 1 / result

print(power_naive(2, 10))   # 1024
print(power_naive(2, -3))   # 0.125
print(power_naive(3.0, 5))  # 243.0
