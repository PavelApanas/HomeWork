
#Вывести первые N цисел кратные M и больше K
print("Enter num K:")
k = int(input())
print("Enter num M:")
m = int(input())
print("Enter num N:")
n = int(input())
list = [i for i in range(1, 100) if i > k and i % m == 0]
first_n = list[:n]
print(first_n)
