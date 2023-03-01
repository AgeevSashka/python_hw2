# Модуль 5
pushkin_year = 1799

answer = 0
day = 6
while answer != pushkin_year:
    answer = int(input('В год роождения А.С.Пушкина'))
    if answer == 1799:
        answer = int(input('А какой день ?'))
        while answer != day:
            if answer == day:
                break
                print('Верно')
            else:
                answer = int(input('А какой день ?'))
        print('Верно')
        break
