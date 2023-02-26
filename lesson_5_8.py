def f_country(city, countries_dict):
    reverse_dict = {}
    for country, cities in countries_dict.items():
        for c in cities:
            reverse_dict[c] = country
    return reverse_dict.get(city, "Город не найден")

# Пример использования:
countries = {
    "Беларусь": ["Минск", "Гродно", "Брест"],
    "Польша": ["Варшава", "Белосток", "Люблин"],
    "Литва": ["Вильнюк", "Каунас", "Клайпеда"]
}

city = "Варшава"
country = f_country(city, countries)
print(f"Город {city} находится в стране {country}")