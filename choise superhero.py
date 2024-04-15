Есть API по информации о супергероях с информацией по всем супергероям.

Напишите функцию для определения самого умного супергероя среди Hulk, Captain America, Thanos.


import requests

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    for hero in response.json():
        name = hero.get('name', '')
        if name in the_smartest_superhero:
            intelligence = int(hero.get('powerstats', {}).get('intelligence', 0))
            the_smartest_superhero[name] = intelligence
    
    # Находим имя самого умного супергероя
    smartest_hero = max(the_smartest_superhero, key=lambda x: the_smartest_superhero[x])
    return smartest_hero

if __name__ == '__main__':
    print(get_the_smartest_superhero())
