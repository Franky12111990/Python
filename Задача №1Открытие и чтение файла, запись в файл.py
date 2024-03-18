def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            ingredients_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingredient = {'ingredient_name': ingredient_info[0], 'quantity': int(ingredient_info[1]),
                              'measure': ingredient_info[2]}
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients
            f.readline()  # пропускаем пустую строку между блюдами

    return cook_book


file_name = 'recipes.txt'
recipes = read_recipes(file_name)
print(recipes)
