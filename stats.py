stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# g = max(stats, key = lambda k: stats[k])
# print(g)

print(max(stats, key=stats.get))






