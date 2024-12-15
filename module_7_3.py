# Задача "Найдёт везде"
import io
from pprint import pprint



class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name,'r', encoding='utf-8') as file:
                list_words = []
                for line in file:
                    item = line.lower()
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        item = item.replace(symbol, ' ')
                    list_words.extend(item.split())
                all_words[file_name] = list_words
        return all_words
    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name , words in all_words.items():
            result[file_name]= words.index(word.lower())+1
        return result
    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name , words in all_words.items():
            result[file_name]= words.count(word.lower())
        return result




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего