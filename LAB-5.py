# Karatsuba Multiplication Algorithm
def karatsuba(x, y):
    # Base case: if numbers are small, multiply directly
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x and y
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    # Recursive calls
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    # Combine results using Karatsuba formula
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


# Example Run
if __name__ == "__main__":
    num1 = 123456789
    num2 = 987654321

    print("First Number:", num1)
    print("Second Number:", num2)
    result = karatsuba(num1, num2)
    print("Multiplication Result (Karatsuba):", result)
