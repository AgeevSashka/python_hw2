# Модуль 2
answer = int(input("Введите Год Рождения А.С.Пушкина :"))

if answer == 1799:
    print('Верно')
    answer = int(input("Введите День Рождения А.С.Пушкина :"))
    if answer == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверно, вы ввели ', answer, ', год рождения А.С.Пушкина 1799')