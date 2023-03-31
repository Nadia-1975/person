# Задание-1
from gettext import install

pip install requests
import requests

from pprint import pprint


TOKEN = '2619421814940190'  # константа токена
urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]  # список адресов


def requests_get(url_all):
    # принимает список адресов
    r = (requests.get(url) for url in url_all)
    return r

def parser():
    # функция парсинга интелекта
    super_man = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Проверте ссылки urls: {urls}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")


parser()






# TOKEN = "y0_AgAAAABpSGeMAADLWwAAAADehcQ7WUPprK7fSPqY6ss7JpsqrI_qgWg"
#
# def test_request():
#     url = "https://httbin.org/get"
#
# class YandexDisk:
#     yandex_url = "https://cloud-api.yandex.net"
#
#
#     def __init__(self, token):
#         self.token = token
#
#
# if __name__ == "__main__":
#     ya = YandexDisk(token=TOKEN)
#     print(ya.Горы.jpeg())




# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "OAuth y0_AgAAAABpSGeMAADLWwAAAADehcQ7WUPprK7fSPqY6ss7JpsqrI_qgWg"
# }

# resp = requests.put("https://cloud-api.yandex.net/v1/disk", headers=headers)
# pprint(resp.json())


# params = {
#     "path": "my_folder_15.03.23"
# }
#
# resp = requests.put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
# print(resp)










