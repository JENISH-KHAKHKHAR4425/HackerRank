#Divide & Conquer With O(log N)
def power_dc_log(x, n):
    if n == 0:
        return 1
    half = power_dc_log(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

# Example
print(power_dc_log(2, 10))  # Output: 1024
