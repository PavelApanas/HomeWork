# **Вывести четные числа от 2 до N по 5 в строку

print("Enter num N:")
n = int(input())
list = [i for i in range(1, n+1)]
first_n = list[:n]
for i in range(0, len(first_n), 5):
    print(*first_n[i:i+5], sep=" ")