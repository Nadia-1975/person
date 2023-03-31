queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'фиша кино',
    'курс доллора',
    'сириалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


words = [len(qry.split()) for qry in queries]

for w in sorted(set(words)):
    print(f"Поисковых запросов, содержащих {w} слов(а): {words.count(w)/len(queries):.0%}")
