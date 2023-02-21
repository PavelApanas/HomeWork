
# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

txt = input("Input text: ")
count = {}
for x in txt:
    if x.isalpha():
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

print(count)