def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y  # Base case for small numbers

    # Calculate the size of the numbers
    size = max(len(str(x)), len(str(y)))
    half_size = size // 2

    # Split the numbers into halves
    a, b = divmod(x, 10**half_size)
    c, d = divmod(y, 10**half_size)

    # Recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    # Combine the results
    result = (10**(2*half_size)) * ac + (10**half_size) * ad_bc + bd

    return result

# Example usage:
num1 = 10
num2 = 10
result = karatsuba(num1, num2)

print(f"The result of {num1} * {num2} using Karatsuba algorithm is: {result}")
