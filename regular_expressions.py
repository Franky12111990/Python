from pprint import pprint
import csv
import re

# Читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Приведение ФИО в нужный формат
def fix_names(contacts):
    for contact in contacts[1:]:
        fullname = ' '.join(contact[:3]).split()
        while len(fullname) < 3:
            fullname.append('')
        contact[:3] = fullname
    return contacts

# Приведение телефонов к нужному формату
def fix_phones(contacts):
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*(доб\.)\s*(\d+))?'
    )
    substitution = r'+7(\2)\3-\4-\5\6\7\8'
    for contact in contacts:
        contact[5] = phone_pattern.sub(substitution, contact[5])
    return contacts

# Объединение дублирующихся записей
def merge_duplicates(contacts):
    contacts_dict = {}
    for contact in contacts[1:]:
        fullname = (contact[0], contact[1])
        if fullname not in contacts_dict:
            contacts_dict[fullname] = contact
        else:
            existing_contact = contacts_dict[fullname]
            for i in range(len(contact)):
                if not existing_contact[i]:
                    existing_contact[i] = contact[i]
    return [contacts[0]] + list(contacts_dict.values())

# Обработка контактов
contacts_list = fix_names(contacts_list)
contacts_list = fix_phones(contacts_list)
contacts_list = merge_duplicates(contacts_list)

pprint(contacts_list)

# Сохранение получившихся данных в другой файл
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
