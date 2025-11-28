#Divide & Conquer - O(N)
def power_dc_linear(x, n):
    if n == 0:
        return 1
    return x * power_dc_linear(x, n - 1)

# Example
print(power_dc_linear(2, 10))  # Output: 1024
