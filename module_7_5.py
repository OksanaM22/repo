#Файлы в операционной системе
import os
import time


for root, dirs, files in os.walk('.'):

  for file in files:

    filepath = os.getcwd()

    filetime = os.path.getctime(filepath)

    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

    filesize = os.stat(filepath).st_size

    parent_dir = os.path.dirname(file)

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')