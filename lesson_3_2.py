# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

print("Enter first value:")
a = int(input())
print("Enter action (+, -, *, /):")
b = input()
print("Enter next value:")
n = int(input())

if b == "*":
    x = a * n
    print("Multiplication:", x)
elif b == ":":
    x = a / n
    print("Division:", x)
elif b == "-":
    x = a - n
    print("Subtract:", x)
elif b == "+":
    x = a + n
    print("Sum:", x)
else:
    print("Error")