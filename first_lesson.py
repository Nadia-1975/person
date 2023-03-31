name = input('Введи Ваше имя: ')

print(f'Здравствуйте, {name}! '
      f'Для получения скидки по Вашей ипотеке ответьте на ряд следующих вопросов')
interest_rate = int(input('Ваша базовая процентная ставка по кредиту: '))
region_code = int(input('Пожалуйста, введите код Вашего региона: '))
number_children = int(input('Пожалуйста, введите количество детей в семье: '))
salary_project = int(input('У Вас есть зарплатный проект в нашем банке? Если ДА, введите 1. Если НЕТ, введите 0: '))
insurance = int(input('Вы хотите оформить страхование в нашем банке? Если ДА, введите 1. Если НЕТ, введите 0: '))
result_string = "ОТВЕТ БАНКА: "


if region_code == 25:
    result = 2
    result_string += "Ваша базовая ставка после применения скидки 'Регион', составляет - " + str(result) + " % \n"
    print(result_string)
else:
    if number_children > 3 and salary_project == 1 and insurance == 1:
        result = interest_rate - 1-0.5-1.5
        result_string += "Ваша базовая ставка по ипотеки после применения скидок 'Дети', 'Зарплатный проект', 'Страхование' уменьшилась на 3% и составляет - " + str(result) + " % \n"
        print(result_string)
    if number_children > 3 and salary_project == 0 and insurance == 1:
        result = interest_rate - 1-1.5
        result_string += "Ваша базовая ставка по ипотеки после применения скидок 'Дети', 'Страхование' уменьшилась на 2.5% и составляет - " + str(result) + " % \n"
        print(result_string)
    if number_children > 3 and salary_project == 0 and insurance == 0:
        result = interest_rate - 1
        result_string += "Ваша базовая ставка по ипотеки после применения скидки 'Дети' уменьшилась на 1% и составляет - " + str(result) + " % \n"
        print(result_string)
    if number_children > 3 and salary_project == 1 and insurance == 0:
        result = interest_rate - 1 - 0.5
        result_string += "Ваша базовая ставка по ипотеки после применения скидок 'Дети', 'Зарплатный проект' уменьшилась на 1.5% и составляет - " + str(result) + " % \n"
        print(result_string)
    if number_children <= 3 and salary_project == 1 and insurance == 1:
        result = interest_rate - 0.5 - 1.5
        result_string += "Ваша базовая ставка по ипотеки после применения скидок 'Зарплатный проект', 'Страхование' уменьшилась на 2% и составляет - " + str(result) + " % \n"
        print(result_string)
    if number_children <= 3 and salary_project == 0 and insurance == 1:
        result = interest_rate - 1.5
        result_string += "Ваша базовая ставка по ипотеки после применения скидок 'Страхование' уменьшилась на 1.5% и составляет - " + str(result) + " % \n"
        print(result_string)
    if number_children <= 3 and salary_project == 1 and insurance == 0:
        result = interest_rate - 0.5
        result_string += "Ваша базовая ставка по ипотеки после применения скидки 'Зарплатный проект' уменьшилась на 0.5% и составляет -  " + str(result) + " % \n"
        print(result_string)
    if number_children <= 3 and salary_project == 0 and insurance == 0:
        result = 0
        result_string += "Вам отказано в скидках: " + str(result) + " % \n"
        print(result_string)

















