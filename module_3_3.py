#Распаковка позиционных параметров
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params( 1, 'строка', True) #принимает три параметра со значениями по умолчанию
print_params()                            # вызов без аргументов
print_params( 2, 'Hallo')           #Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов

print_params(b = 25)                      #работают ли вызовы print_params(b = 25)
print_params(c = [1,2,3])                 #работают ли вызов print_params(c = [1,2,3])

values_list = [False, [1, 2, 3]]
values_dict = {'c': 'Oksana'}
print_params (*values_list, **values_dict)  #Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

values_list_2 = [54.32, 'Строка' ] #3.Распаковка + отдельные параметры:
print_params(*values_list_2, 42)



