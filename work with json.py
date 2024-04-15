Условие задачи
Вам дан json-файл с новостями. Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.

Приведение к нижнему регистру не требуется.


import json

def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open(file_path, "r") as f:
        json_data = json.load(f)
    dict_news = json_data["rss"]["channel"]["items"]
    text_news = []
    for news in dict_news:
        description = [
            word for word in news["description"].split(" ") if len(word) > word_max_len
        ]
        text_news.extend(description)

    unique_word = set(text_news)
    d = {}
    for i in unique_word:
        for m in text_news:
            if i == m:
                d.setdefault(i, 0)
                d[i] += 1

    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    res = [word for word in d][:top_words_amt]
    return res

if __name__ == '__main__':
    print(read_json('newsafr.json'))
