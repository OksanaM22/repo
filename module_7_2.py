# Задача "Записать и запомнить"
from idlelib.iomenu import encoding
from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    file = open('test.txt', 'w', encoding='utf-8')
    for line_number, item in enumerate(strings, start = 1):
        position = file.tell()
        strings_positions[line_number, position] = item #создание словаря
        file.write(f'{item}\n')
    file.close()
    return strings_positions


info = [

    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)