x = ['2018-01-01', 'yandex', 'cpc', 100]


y = {x[-2]: x[-1]}
for i in x[:-2][::-1]:
    y = {i: y}
print(y)

