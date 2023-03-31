boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Liza']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print("Предупреждение! Кто-то может остаться без пары!")
else:

    boys.sort(key=str.lower)
    girls.sort(key=str.lower)

    ideal_couples = zip(boys, girls)
    print("Идеальные пары:")
    for boy, girl in zip(boys, girls):
        print(f"{boy} и {girl}")



#dict
#.items()



