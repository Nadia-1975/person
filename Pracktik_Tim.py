







#------1. Работа с текстом.-----

# name = input("Ваше имя: ")
# print(name)
# print(type(name))

# x = name
# print(x, type(x))

# a = 1
# b = 2
# print(a, '+', b, '=', a+b)
# print(a, b, sep=':')
# print(a, b, sep='\n')
# print(a, b, sep='\n\n')
# print(a, b, sep='\t')
# print(a, b, sep='\\')
# print(a, b, a+b, end='')

# s = '''"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"'''
# s1 = "oooooooooooooooooooooo"
# print(s, s1, sep='\n')
# print(5+7)
# print('5'+'7')

# name = 'Pol'
# print(type(name))
# print(dir(name))
# help(str)

# s = "hELlo"
# s.lower()
# s.upper()
# s.title()
# s.replace('E', 'A')
# print(s)
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.replace('E', 'A'))
# print(len(s))

# for char in "1АБСДЕЕЁЖЗ7":
#     print(char, '-', ord(char), end=',   ')

# for c1 in "ABCD":
#     for c2 in "1234":
#         print(c1, c2)

# s = 'СТРОКА'
# print(s)
# print(s[0])
# print(s[-1])
# print(s[0:5])
# print(s[0:4:3])
# print(len(s))
# print(s[3:len(s)])

# file = open('my.txt', 'w')
# file.writelines(["Ехал грека,\n",
#                  "Через реку,"])
# file.close()
# for line in open('my.txt'):
#     print(line)
# file.close()

# with open('my.txt') as file:
#     for line in file:
#        # print(line)
#        print(line.strip())

# print('кот' > 'кит')
# print('кот' > 'котёнок')

# class Person:
#     def __init__(self, id):
#         self.id = id
# some_person = Person(100)
# some_person.__dict__['age'] = 30
# print(some_person.age + len(some_person.__dict__))

# class Income:
#     def __init__(self, id_):
#         self.id_ = id_
#         id_ = 100
# income_1 = Income(1000)
# print(income_1.id_)

class Primate:
    def eat(self, food):
        print(food)
class Man(Primate):
    def eat(self, food, cooked=False):
        if cooked:
            print(cooked, food)
        else:
            print(food)


















