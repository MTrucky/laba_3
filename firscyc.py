def sum_nested(lst):
    total =  0
    stack = [lst]

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            total += current

    return total
print(sum_nested([1, [2, [3,  4, [5]]]])) 
