# УСЛОВНЫЕ ВЫРАЖЕНИЯ
# ОПЕРАЦИИ СТРАВНЕНИЯ
# == равно
# != не равно
# < > меньше больше
# <= >= меньше-равно больше - равно

# a = 5
# b = 6
# result = a < b or a == b # можем изменить or на and и получим другой ответ(умножение двух булевых значений)
# print(result)

# оператор in
# значение n набор значений

# message = 'hello world'
# message1 = 'hello'
# print(message1 in message)

# УСЛОВНАЯ КОНСТРУКЦИЯ
# if логическое выражение:
#       инструкции
# elif логическое выражение:
#       инструкции
# else:
#       инструкции


# language = input('Введите язык: ')
# if language == 'английский' or language == 'english':
#     print('Добро пожаловать на курс по изучения английского языка!')
# elif language == 'русский' or language == 'russian':
#     print('Добро пожаловать на курс по изучения русского языка!')
# elif language == 'немецкий' or language == 'germany':
#     print('Добро пожаловать на курч по изучению немецкого языка!')
# else:
#     print('Вы ввели некорректные данные!')


# letter = input('Введите букву: ')
# if letter == 'a'or letter == 'e' or letter == 'i' or letter =='o' or letter =='u':
#     print('Эта буква гласная!')
# elif letter == 'y':
#     print('Эта буква может быть как гласной, так и согласной!')
# else:
#     print('Эта буква согласная!')

# num = int(input('Введите целое число: '))
# if num % 2 == 0:
#     print('Четное число')
# else:
#     print('Нечетное число')

# ЦИКЛЫ

# a = 'hello'
# for item in a:
#     if a[0] in a:
#         b = a[0].upper()
#         print(b)
#         break


# ИТЕРАЦИЯ СО СПИСКОМ С ФУНКЦИЕЙ range()

# for i in range(0,11,2): #(start, stop, step)
#     print(i)

# for i in range(10,0,-1):
#     print(i)


# num = int(input()) # 3
# maxx = 0
# for i in range(num): # 3,10,25,12
#     a = int(input())
#     if a % 5 == 0 and a > maxx:
#         maxx = a
# print(maxx)

# num = int(input())
# maxx = 0
# while num != 0:
#     if num % 5 == 0 and num > maxx:
#         maxx = num
#     num = int(input())
# print(maxx)

