import pytest
import hw_lesson4


@pytest.mark.parametrize(
    "list, etalon",
    [
        ([
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
         ],
         [{'visit1': ['Москва', 'Россия']},
          {'visit3': ['Владимир', 'Россия']},
          {'visit7': ['Тула', 'Россия']},
          {'visit8': ['Тула', 'Россия']},
          {'visit9': ['Курск', 'Россия']},
          {'visit11': ['Архангельск', 'Россия']},
          {'visit12': ['Новосибирск', 'Россия']}]
        ),
        ([
            {'visit1': ['Москва', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']}
        ],
        [
            {'visit1': ['Москва', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']}
        ]
        )
    ])
def test1(list, etalon):
    res = hw_lesson4.task1(list)
    assert res == etalon


@pytest.mark.parametrize("ids, etalon", [
    ({'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]},
     [{213, 15, 54, 119, 98, 35}]),
    ({'user1': [213, 600, 600, 600, 213],
      'user2': [54, 54, 54, 119, 119]},
     [{213, 600, 54, 119}])
])
def test2(ids, etalon):
    res = hw_lesson4.task2(ids)
    assert res == etalon

@pytest.mark.parametrize("stats, etalon", [
    ({'facebook': 55, 'yandex': 11111, 'vk': 554, 'google': 999, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 55, 'yandex': 1, 'vk': 51154, 'google': 999, 'email': 42, 'ok': 98}, 'vk')])
def test4(stats, etalon):
    res = hw_lesson4.task4(stats)
    assert res == etalon
