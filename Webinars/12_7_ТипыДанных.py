# # регистрочуствительный язык
# name = 'Ivan'
# Name = 'Ivan'
# # две разные переменные
# # camel case
# userName = 'Tom'
# # snake case
# user_name = 'Bill'
#
#
# # DATE TYPES
# # типизация: динамическая и статическая
# # Java, C++ и тд.  string name = 'Ivan'
# # в Python не обязос указывать тип(он сам воспринимает)
#
# # NUMBERS
# # целые и дробные(числа с плавающей точкой)
# a = 5 + 5
# b = 5.3 + 10
# print(a)
# print(b)
#
#
# # ДЕЛЕНИЕ
# # / - обычное // - целочисленное % - остаток от деления
# a = 5 / 2
# b = 5 // 2
# с = 5 // 2
# print(a)
# print(b)
# print(с)
#
#
# a = 10**3
# print(a)
# # возведение в степень
#
#
# # ПРОВЕРКА на >/</==
#
# a = 8 > 3
# print(a)
# b = 1 == 1
# print(b)
# c = 8 < 3
# print (c)
#
#
# # ОКРУГЛЕНИЕ
#
# a  = round(10/3, 2)
# print(a)
#
# b = round (10/3)
# print(b)
#
# c = 10/3
# print(c)
#
#
# # ФУНКЦИЯ ПРЕОБРАЗОВАНИЯ - int() целочисленное преобразование
# a = 10/3.0
# b = int(a)
# print(b)
#
#
# # float() - вещественное преобразование(число с плавающей точкой)
# # bin() - перевод из десятичного числа в двоичное
#
# print(bin(8))
#
#
# import math
# print(math.pow(2, 6))
# # возведение в степень
# print(math.sqrt(9))
# # взять корень
# print(math.pi)
#
#
# # String
# # '', "", ''' ''',
# name = "Иван"
# print(name)
# # можно вывести букву по индексу(индекс начинатся с 0)
# print(name[0])
# print(name[2])
# print(name[-1])
#
# name = "Иван"
# fullname = "Иванович"
# # срез строки [start:stop:step]
# print (name[1:3])
# print(name[1:6:2])
#
# concat
# res = name + fullname + ' привет!'
# print(res)
#
# # Methods string
# string = 'Hello!'
# res = string.lower()
# print(res)
# # делает все буквы маленькими
# res = string.upper()
# print(res)
# # делает все буквы заглавными
#
#
# # делаем программу которая запрашивает данные на ввод имени и переформатирует текст в стандарт написания с загл буквы
# name = input('Введите Ваше имя ')
# name_start = name[0].upper()
# name_end = name[1:].lower()
# res = name_start + name_end
# print(res)
#
#
# # for..in
#
# name = 'Ivan'
# for i in name:
#     print(i)
# # сделали перебор всех символов с новой строчки
#
# exm = 'Привет мир'
# count = 0 # сделали счетчик
# for i in exm:
#     if i == 'и':
#         count = count + 1 # счетчик добавляет +1 каждый раз когда находит символ "и"
# print(count, 'буквы "и" данной строке')
#
#
# # проверка на вхождения
# # in и not in
# a = 'hello'
# b = 'hello world'
# print(a in b)
#
#
# # len() показывает сумму символов в строке
# string = 'hello'
# print(len(string))
#
# # split() разбивает строки по разделителю
# # join() собирает строку из списка
#
# #\n переход на следующую строчку
# print('hello\nworld')
#
#
# # format
# #{} можно задать порядок по ключевым словам
#
# string = "{a},{b},{c}".format(a='Петя', c='Ваня',b='Катя')
# print(string)
#
#
# # F - СТРОКИ
#
# # простой синтаксис
# name = 'Eric'
# age = 24
#
# print(f'Hello, {name}. You are {age}.')
#
#
# print(f"{2*37}")
#
#
# # List - [], list()
# numbers = [1,2,3,4, 'hello', True]
# numbers_1 = list()
# print(numbers_1)
# print(numbers)
#
#
# people = ['Ivan', 'Tom', 'Kate']
# for person in people:
#     print(person)
#
#
# #Methods list
#
# #append(item) добавляет элемент в список
# people = ['Ivan', 'Tom', 'Kate']
# new_person = people.append('Bob')
# # insert(item) - добавляет элемент в список по индексу
# print(people.insert(2,'Bill'))
# #remove(item) удаляет элемент(только первый попавшийся
# print(people.remove('Bill'))
# print(people)
#
# # in
# people = ['Ivan', 'Tom', 'Kate']
# if 'Tom' in people:
#     people.remove('Tom')
# print(people)
#
#
# #count()
# people = ['Ivan', 'Tom', 'Kate','Tom']
# people_count = people.count('Tom')
# print(people_count)
#
#
# a = [4,3,2,1]
# print(sorted(a)) #сортирует по порядку
#
# people = [
#     ['Ivan', 29],
#     ['Kate', 31],
#     ['Bob',45]
#
# print(people[0][1]) #выводим второй элемент из первого списка
#
#
# Tuple () похож на список но отличается тем что он является неизменяемым
#
# # СЛОВАРИ {keys:values}
# users = {1:'Tom',2:'Bob',3:'Kate'}
# users[1]='Tom2'
# print(users)
#
# users = {1:'Tom',2:'Bob',3:'Kate'}
# users_1 = users.get(3)
# print(users_1) #вытаскиваем значение через обращние по ключу
#
# users = {1:'Tom',2:'Bob',3:'Kate'}
# # items()
# for key, value in users.items():
#     print(key,value) # получаем пару: ключ - значение
#
# # МНОЖЕСТВА set()
#
# users = {'Tom','Bob','Kate'}
# print(users) # каждый раз выводит в разной последовательности, все элементы уникальны
#
# # union() - объединение
# users_1 = {'Tom','Bob','Kate'}
# users_2 = {'Sam','Kirill','Alex'}
# users_3 = users_1.union(users_2)
# print(users_3)
