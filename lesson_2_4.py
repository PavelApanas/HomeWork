#2.4
#Пользователь вводит 3 числа, сказать сколько из них положительных
#и сколько отрицательных

num1 = float(input("Введите 1 число: "))
num2 = float(input("Введите 2 число: "))
num3 = float(input("Введите 3 число: "))


pos = (num1 > 0) + (num2 > 0) + (num3 > 0)
neg = (num1 < 0) + (num2 < 0) + (num3 < 0)


print("Sum_positive:", pos)
print("Sum_negative:", neg)