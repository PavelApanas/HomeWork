def shift_list(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]