def sorted_lst(lst):
    sorted_lst = sorted(lst, key=lambda x: (x % 2 == 0, x))
    return sorted_lst

lst = [3, 7, 2, 8, 1, 6, 4, 5]
sorted_lst = sorted_lst(lst)
print(sorted_lst)