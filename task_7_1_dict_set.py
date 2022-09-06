# Создайте словарь, в котором будут храниться словари с данными о вашей семье (или вымышленной семье).
# Обязательные элементы : несколько человек (имен), их роль в семье (родитель\сын\брат и т.п.),
# возраст, город проживания. (4-6 человек). Вывести на экран отдельно ключи и отдельно значения

family = {
    'Mother': {
        'Name': 'Valentina',
        'Age': '60',
        'City': 'Gomel'
    },
    'Sister': {
        'Name': 'Tania',
        'Age': '35',
        'City': 'Brest'
    },
    'Wife': {
        'Name': 'Alina',
        'Age': '35',
        'City': 'Gomel'
    },
    'Cat': {
        'Name': 'Fania',
        'Age': '5',
        'City': 'Moscow'
    },
    'Bird': {
        'Name': 'Jonny',
        'Age': '138',
        'City': 'London'
    }
}
print(family)
print(family.keys())
print(family.values())
