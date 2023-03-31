data = int(input('Введите дату Вашего рождения: '))
month = int(input('Введите месяц(число от 1 до 12) Вашего рождения: '))

if data >= 22 and month >= 12 or data <= 20 and month <=1:
    result = 'Козерог'
    print('ВЫВОД: Вы', str(result), '- дотошны, умны и деятельны.')
elif data >= 21 and month >= 1 or data <= 19 and month <=2:
    result = 'Водолей'
    print('ВЫВОД: Вы', str(result), '- темпераментны, независимы и изменчивы.')
elif data >= 20 and month >= 2 or data <= 20 and month <=3:
    result = 'Рыба'
    print('ВЫВОД: Вы', str(result), '- мудры, отзывчивы и чувствительны.')
elif data >= 21 and month >= 3 or data <= 20 and month <=4:
    result = 'Овен'
    print('ВЫВОД: Вы', str(result), '- инициативны, последовательны и педантичны.')
elif data >= 21 and month >= 4 or data <= 21 and month <=5:
    result = 'Телец'
    print('ВЫВОД: Вы', str(result), '- терпеливы, трудолюбивы и созидательны.')
elif data >= 22 and month >= 5 or data <= 21 and month <=6:
    result = 'Близнец'
    print('ВЫВОД: Вы', str(result), '- любопытны, нежныи добры.')
elif data >= 22 and month >= 6 or data <= 22 and month <=7:
    result = 'Рак'
    print('ВЫВОД: Вы', str(result), '- интуитивны, эмоциональны и умны.')
elif data >= 23 and month >= 7 or data <= 23 and month <=8:
    result = 'Лев'
    print('ВЫВОД: Вы', str(result), '- горделивы, самоуверенныи амбициозны.')
elif data >= 24 and month >= 8 or data <= 22 and month <=9:
    result = 'Дева'
    print('ВЫВОД: Вы', str(result), '- элегантны, организованны и добры.')
elif data >= 23 and month >= 9 or data <= 22 and month <=10:
    result = 'Весы'
    print('ВЫВОД: Вы', str(result), '- дипломатичны, артистичны и интеллигентны.')
elif data >= 23 and month >= 10 or data <= 22 and month <=11:
    result = 'Скорпион'
    print('ВЫВОД: Вы', str(result), '- сильны, эмоциональны и независимы.')
elif data >= 23 and month >= 11 or data <= 21 and month <=12:
    result = 'Стрелец'
    print('ВЫВОД: Вы', str(result), '- харизматичны, энергичны и деятельны.')




