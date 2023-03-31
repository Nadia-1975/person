# ЗАДАЧА-1
# from pprint import pprint
# f = open('task1.txt', 'w')
# f.writelines(['Омлет\n', ' 3\n', 'Яйца\t|', '  2\t|', ' шт.\n',
#                  'Молоко\t|', '  100\t|', ' мл.\n',
#                  'Помидор\t|', '  2\t|', ' шт.\n\n',
#               'Утка по-пекински\n', ' 4\n', 'Утка\t    |', '  1\t|', ' шт.\n',
#                  'Вода\t    |', '  2\t|', ' л.\n',
#                  'Мёд\t        |', '  3\t|', ' ст. ложки\n',
#                  'Соевый соус\t|', '  60\t|', ' мл.\n\n',
#               'Запеченный картофель\n', ' 3\n', 'Картофель\t  |', '  1\t|', ' кг.\n',
#                  'Чеснок\t      |', '  3\t|', ' зубчик\n',
#                  'Сыр гауда\t  |', ' 100\t|', ' гр.\n\n'])
#
# f.close()
# #
# f = open('task1.txt', 'r')
# f.readlines()
# print(f.readlines())
#______________________________________----------------------------------------
# 1) определяем строка чило или нет ? (ПАША)
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False
#
#
# with open('recipes.txt', 'rt', encoding='utf-8') as file:
#     cook_book = {}
#     ingredients = []

#читаем файл по строчно, проверяем из (Паша)
    # скольких слов состоит строка и является ли числом,
    # если слов меньше 3 то это название блюда, если число то пропускаем строку и далее по алгоритму (ПАША)
#     for line in file:
#         if line != '\n':
#             if len(line.split(' ')) < 3:
#                 if not is_number(line):
#                     dish_name = line
#                     cook_book[dish_name] = []
#             else:
#                 ingredient_name, quantity, measure = line.split('|')
#                 cook_book[dish_name].append(
#                     {'ingredient_name': ingredient_name,
#                      'quantity': quantity,
#                      'measure': measure}
#                 )
#
# print(cook_book)

#-----------------------------------------------------------------
# Задание-1
# from pprint import pprint
#
# with open('recipes.txt', 'rt', encoding='utf-8') as file:
#     cook_book = {}
#     for line in file:
#         dish_name = line.strip()
#         ingredient_count = int(file.readline())
#         ingredients = []
#         for _ in range(ingredient_count):
#             ingredient = file.readline().strip()
#             ingredient_name, quantity, measure = ingredient.split('|')
#             ingredients.append(
#                 {'ingredient_name': ingredient_name,
#                  'quantity': quantity,
#                  'measure': measure}
#             )
#         cook_book[dish_name] = ingredients
#         file.readline()
#
# pprint(cook_book)

# Задача 1
# cook_book = {}
# with open('recipes.txt', encoding='utf-8') as src_file:
#     last_key = ''
#     for line in src_file:
#         line = line.strip()
#         if line.isdigit():
#             continue
#         elif line and '|' not in line:
#             cook_book[line] = []
#             last_key = line
#         elif line and '|' in line:
#             name, qt, msure = line.split(" | ")
#             cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))
#
# pprint(cook_book)

# Задача 2
# from pprint import pprint
#
# def dict_collector(file_path):
#     with open(file_path, 'r', encoding ='utf 8') as file_work:
#         menu = {}
#         for line in file_work:
#             dish_name = line[:-1]
#             counter = file_work.readline().strip()
#             list_of_ingridient = []
#             for i in range(int(counter)):
#                 dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # временный словарь
#                 ingridient = file_work.readline().strip().split(' | ') # перемещение по файлу
#                 for item in ingridient:
#                     dish_items['ingredient_name'] = ingridient[0]
#                     dish_items['quantity'] = ingridient[1]
#                     dish_items['measure'] = ingridient[2]
#                 list_of_ingridient.append(dish_items)
#                 cook_book = {dish_name: list_of_ingridient}
#                 menu.update(cook_book)
#             file_work.readline()
#
#     return(menu)
#
# dict_collector('recipes.txt')
#
# def get_shop_list_by_dishes(dishes, persons=int):
#
#     menu = dict_collector('recipes.txt')
#     print('Ознакомьтесь с Нашим меню :')
#     pprint(menu)
#     print()
#     shopping_list = {}
#     # pprint(menu.keys())
#     try:
#         for dish in dishes:
#             for item in (menu[dish]):
#                 # print(item['ingredient_name'])
#                 # print(item['measure'])
#                 # print(item['quantity'])
#                 items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
#                 if shopping_list.get(item['ingredient_name']):
#                     # print(f' Такое {items_list} уже есть в списке. Добавил еще')
#                     extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
#                                   int(items_list[item['ingredient_name']]['quantity']))
#                     # print(extra_item)
#                     shopping_list[item['ingredient_name']]['quantity'] = extra_item
#
#                 else:
#                     # shopping_list[item['ingredient_name']]['quantity'] *= persons
#                     shopping_list.update(items_list)
#
#         print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
#         pprint(shopping_list)
#     except KeyError:
#         print("Вы ошиблись в названии блюда, проверьте ввод")
#
#
# get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)

# Задача 3

def rewrite_file(path1=None, path2=None, path3=None):
    if  path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        os.chdir('sorted')
        out_file = "rewrite_file.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(out_file, 'w', encoding='utf-8') as f_total:

            if  (file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif  (file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif  (file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('УПС')
    return
f = open('finish_file.txt')
res = f.read()
print(res)
f.close()

