import requests
from bs4 import BeautifulSoup
import json

# URL для поиска вакансий
url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"

# Отправка запроса
response = requests.get(url)
response.raise_for_status()  # Проверка на успешное выполнение запроса

# Парсинг HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Найдем все вакансии на странице
vacancies = soup.find_all('div', class_='vacancy-serp-item')

vacancies_data = []

# Перебор всех найденных вакансий
for vacancy in vacancies:
    title = vacancy.find('a', class_='bloko-link').text
    link = vacancy.find('a', class_='bloko-link')['href']
    company = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text
    city = vacancy.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
    salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
    salary = salary.text if salary else 'Не указана'

    # Отправка запроса на страницу вакансии для получения описания
    vacancy_response = requests.get(link)
    vacancy_response.raise_for_status()
    vacancy_soup = BeautifulSoup(vacancy_response.text, 'html.parser')

    # Проверка наличия ключевых слов в описании
    description = vacancy_soup.find('div', {'data-qa': 'vacancy-description'}).text.lower()
    if 'django' in description and 'flask' in description:
        vacancy_data = {
            'title': title,
            'link': link,
            'company': company,
            'city': city,
            'salary': salary
        }
        vacancies_data.append(vacancy_data)

# Запись данных в JSON файл
with open('vacancies.json', 'w', encoding='utf-8') as f:
    json.dump(vacancies_data, f, ensure_ascii=False, indent=4)

print(f'Найдено {len(vacancies_data)} вакансий.')
