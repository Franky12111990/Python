Вам дан xml-файл с новостями. Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.

Приведение к нижнему регистру не требуется.



import xml.etree.ElementTree as ET
from collections import Counter

def read_xml(file_path, word_min_len=7, top_words_amt=10):
    """
    Функция для чтения файла с новостями в формате XML и вывода топ-10 самых часто встречающихся слов длиннее 6 символов.
    """
    try:
        # Парсим XML файл
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Получаем текст из всех элементов 'description'
        all_words = []
        for item in root.findall('.//item'):
            description = item.find('description').text
            if description:
                all_words.extend(description.split())
        
        # Фильтруем слова по длине и подсчитываем их частоту
        filtered_words = [word for word in all_words if len(word) >= word_min_len]
        word_counts = Counter(filtered_words)
        
        # Возвращаем топ-10 наиболее часто встречающихся слов
        return [word for word, _ in word_counts.most_common(top_words_amt)]
    
    except Exception as e:
        print("Ошибка при чтении XML файла:", e)
        return []

if __name__ == '__main__':
    print(read_xml('newsafr.xml'))
