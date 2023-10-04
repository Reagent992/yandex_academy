"""
Имя of the month
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/mCnOyeyeV8
Статус: Решено.
"""


def month(number, locale):
    ru_month = {
        1: 'Январь',
        2: 'Февраль',
        3: 'Март',
        4: 'Апрель',
        5: 'Май',
        6: 'Июнь',
        7: 'Июль',
        8: 'Август',
        9: 'Сентябрь',
        10: 'Октябрь',
        11: 'Ноябрь',
        12: 'Декабрь',
    }
    en_months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    if locale == 'ru':
        return ru_month[number]
    elif locale == 'en':
        return en_months[number]


if __name__ == '__main__':
    assert month(1, 'en') == 'January'
    assert month(7, 'ru') == 'Июль'
