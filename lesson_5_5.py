def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        j = n - i - 1
        lst[i], lst[j] = lst[j], lst[i]
    return lst

lst = [1, 2, 3, 4, 5]
reversed_lst = reverse_list(lst)
print(reversed_lst)