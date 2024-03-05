def calculate_a(k):
    a, b = 1, 1
    for _ in range(k-1):
        a = 0.5 * (b ** 0.5 + 0.5 * a ** 0.5)
        b = a 
    return a

print(calculate_a(5))
