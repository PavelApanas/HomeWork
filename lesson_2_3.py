name = input("Введите свое имя: ")
age = input("Введите свой возраст: ")
city = input("Введите название города: ")


message_1 = "Привет, %s! Вам - %s лет и Вы проживаете в г. %s." % (name, age, city)
message_2 = "Привет, {}! Вам - {} лет и Вы проживаете в г. {}.".format(name, age, city)
message_3 = f"Привет, {name}! Вам - {age} лет и Вы проживаете в г. {city}."

print(message_1)
print(message_2)
print(message_3)