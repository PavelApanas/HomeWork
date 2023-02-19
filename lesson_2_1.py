
#2.1
#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
#способами


s = input("Введите предложение: ")
result_1 = "-".join(s.split())
result_2 = s.replace(" ", "-")
print(result_1)
print(result_2)