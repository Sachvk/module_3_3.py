#1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])


#2.Распаковка параметров:
# def print_params(a, b, c):
#     print(a, b, c)
values_list = [10, 'строка', False]
values_dict = {'a' : 10, 'b' : 'строка', 'c' : False}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

