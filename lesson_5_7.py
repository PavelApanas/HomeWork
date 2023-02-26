def sum_n(lst):
    result = []
    for i in range(len(lst)):
        if i == 0:  # для первого элемента
            n_sum = lst[i+1] + lst[-1]
        elif i == len(lst) - 1:  # для последнего элемента
            n_sum = lst[0] + lst[i-1]
        else:  # для остальных элементов
            n_sum = lst[i-1] + lst[i+1]
        result.append(n_sum)
    return result


lst = [1, 2, 3, 4, 5]
result = sum_n(lst)
print(result)