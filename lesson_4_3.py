
# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input("Input number: "))
list_dict = {}
for x in range(n):
    name = input(f"Input name {x}: ")
    email = input(f"Input email {x}: ")
    list_dict[x] = {"name": name, "email": email}
print(list_dict)