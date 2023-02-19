
#2.1
#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
#способами

#variant_1
s = input("Введите предложение: ")
result = "-".join(s.split())
print(result)


#variant_2

s = input("Введите предложение: ")
result = s.replace(" ", "-")
print(result)