from pprint import pprint


#########Task1#######################################
geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Лиссабон', 'Португалия']},
        {'visit11': ['Архангельск', 'Россия']},
        {'visit12': ['Новосибирск', 'Россия']}
    ]
def task1(geo_logs):
    print('Задание 1\n')
    n = 0
    while n < len(geo_logs):

        for key, value in geo_logs[n].items():
            if value[1] != 'Россия':

                del (geo_logs[n])
                n -= 1

            else:
                n += 1

    print('Список, содержащий только визиты из России:')
    print()
    pprint(geo_logs)
    return geo_logs

    #########Task2##########################################
ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
def task2(ids):
    print('\nЗадание 2\n')
    set_unicum = set()

    for key, value in ids.items():
        set_unicum = set(value) | set_unicum

    print('Уникальные  гео-ID из значений словаря ids:')
    print([set_unicum])
    return [set_unicum]

    #########Task3#########################################
def task3():
    print('\nЗадание 3\n')
    queries = [
        'смотреть    сериалы,онлайн',
        'новости спорта',
        'афиша / кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по ! питону',
        'сериалы про спорт для детей до 16 лет',
        'сериалы про спорт для детей до 16 лет',
        'шоу',
        'кинокомедии,2022 и 2021'
    ]
    list_count = []

    print('Доля вхождения в список запросов:')
    for query in queries:

        symbols = ',.-/;:?/\|!=+'

        for letter in query:
            if letter in symbols:
                query = query.replace(letter, " ")

        query = query.split()
        counter = len(query)  # количество слов в запросе
        list_count.append(counter)
    dict = {}

    for element in set(list_count):
        percent = int(list_count.count(element) / len(list_count) * 100)
        dict[element] = percent

        print(f'Запрос из {element} слов(а)  = {percent} %')
    return dict

    #########Task4#########################################
stats = {'facebook': 55, 'yandex': 11120, 'vk': 1154, 'google': 99, 'email': 42, 'ok': 98}
def task4(stats):
    print('\nЗадание 4\n')
    print(f'Канал с максимальным объемом продаж: {(max(stats, key=stats.get))}')
    return (max(stats, key=stats.get))


    #########Task5#########################################
def task5():
    print('\nЗадание 5\n')

    list = [['2018-01-01', 'yandex', 'cpc', 100], ['2019-01-01', 'google', 'cpc', 90],
            ['2018-01-01', 'mail.ru', 'cpc', 150]]
    dict = []
    for i in list:
        dict1, dict2, dict3 = {}, {}, {}
        dict1[i[-1]] = i.pop(-1)
        dict2[i[-2]] = dict1
        dict3[i[-3]] = dict2
        dict.append(dict3)
    pprint(dict)
    return dict
