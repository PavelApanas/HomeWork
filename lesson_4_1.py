#Заполнить список степенями числа 2 (от 2^1 до 2^n).

print("Enter num N:")
n = int(input())
x = []
for i in range(1, n+1):
    z = 2 ** i
    x.append(z)
    print(f"2 в степени {i+1} равно {z}")