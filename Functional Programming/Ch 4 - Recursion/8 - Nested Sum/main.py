def sum_nested_list(lst):
    current = 0
    for i in range(len(lst)):
        if isinstance(lst[i], int):
            current += lst[i]
        elif isinstance(lst[i], list):
            current += sum_nested_list(lst[i])
    return current

