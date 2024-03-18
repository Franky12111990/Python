import os

# Получаем список файлов в папке
folder_path = os.getcwd()
file_names = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

# Создаем список для хранения информации о файлах (имя файла, количество строк, содержимое)
files_info = []

# Получаем информацию о файлах
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_info = {
            'name': file_name,
            'line_count': len(lines),
            'content': lines
        }
        files_info.append(file_info)

# Сортируем список файлов по количеству строк
files_info.sort(key=lambda x: x['line_count'])

# Записываем содержимое файлов в результирующий файл
result_file_path = 'result.txt'  # Укажите путь к результирующему файлу
with open(result_file_path, 'w', encoding='utf-8') as result_file:
    for file_info in files_info:
        result_file.write(f"{file_info['name']}\n")
        result_file.write(f"{file_info['line_count']}\n")
        for line in file_info['content']:
            result_file.write(line)

print("Результирующий файл успешно создан.")
