documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
"""
def get_name(doc_number):
   for element in documents:
      if element["number"] == doc_number:
         return element["name"]

print(get_name("10006"))

def get_directories(doc_number):
   for k,v in directories.items():
       if doc_number in v:
           return k


print(get_directories('10006'))
print(get_directories('11-2'))

def add_document(type, number, name, shelf_number):
    documents.append({'type':type, 'number':number, 'name':name})
    directories[shelf_number] = [number]
    return 0
add_document("письмо", "26252423", "вася пупкин", "4")


for x in documents:
   print (x)
for k,v in directories.items():
    print (k,v)
"""


def get_name(doc_number):
    for element in documents:
        if element["number"] == doc_number:
            return element["name"]
    return "Документ не найден"


def get_directory(doc_number):
    for k, v in directories.items():
        if doc_number in v:
            return k
    return "Полки с таким документом не найдено"


def add(document_type, number, name, shelf_number):
    documents.append({'type': document_type, 'number': number, 'name': name})
    directories[shelf_number].append(number)


# не меняйте эту часть программы
# проверка работы реализованных функций
print(get_name("10006"))
print(get_directory("11-2"))
print(get_name("101"))
add('international passport', '311 020203', 'Александр Пушкин', '3')
print(get_directory("311 020203"))
print(get_name("311 020203"))
print(get_directory("311 020204"))
