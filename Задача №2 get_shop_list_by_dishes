# Импортируем функцию read_recipes из файла recipes.py
from recipes import read_recipes


# Определяем функцию get_shop_list_by_dishes
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_recipes('recipes.txt')
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity

    return shop_list


# Вызываем функцию get_shop_list_by_dishes с нужными аргументами
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)
