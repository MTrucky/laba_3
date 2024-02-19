def calculate_a(k, a=1, b=1):
    if k ==  1:
        return a
    else:
        a_prev = calculate_a(k -  1, a, b)
        b_prev = calculate_a(k -  1, a, b)
        
        a_k =  0.5 * (b_prev **  0.5 +  0.5 * a_prev **  0.5)
        
        return a_k

print(calculate_a(5)) 
