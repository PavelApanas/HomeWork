def filter_strings(lst):
    return filter(lambda x: isinstance(x, str), lst)

lst = [1, 'hello', 3.14, True, 'world']
filtered_lst = filter_strings(lst)
for s in filtered_lst:
        print(s)