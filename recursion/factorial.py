def factorial(n: int):
    if n >= 2:
        n *= factorial(n - 1)
    return n


print(factorial(4))  # 24
