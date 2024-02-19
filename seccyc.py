def calculate_a(k):
    
    a = b =  1

    for i in range(2, k +  1):
        a, b = b, (0.5 * (b **  0.5 +  0.5 * a **  0.5))
    
    return a
print(calculate_a(5))  
