#2.2
# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

a = float(input("Insert number 1 "))
b = float(input("Insert number 2: "))
c = float(input("Insert number 3 "))

avg = (a + b + c) / 3
avg_rounded = round(avg, 3)

print("AVG", avg_rounded)