# Модуль 6
# Александр Пушкин
push = 'Александр Пушкин'
push_year = 1799
push_day = 6
# Михаил Лермонтов
ler = 'Михаил Лермонтов'
ler_year = 1814
ler_day = 15
# Лев Толстой
leo = 'Лев Толстой'
leo_year = 1828
ler_day = 6
# Владимир Путин
put = 'Владимир Путин'
put_year = 1952
put_day = 7
# Михаил Ломоносов
lom = 'Михаил Ломоносов'
lom_year = 1711
lom_day = 19
i = 0
while i < 1:
    reply = 0
    rereply = 0
    answer = int(input('В каком году родился ' + push))
    if answer == push_year: # Правильный ответ 1799
        reply += 1
    else:
        rereply += 1

    answer = int(input('В каком году родился ' + ler))
    if answer == ler_year: # Правильный ответ 1814
        reply += 1
    else:
        rereply += 1

    answer = int(input('В каком году родился ' + leo))
    if answer == leo_year: # Правильный ответ 1828
        reply += 1
    else:
        rereply += 1

    answer = int(input('В каком году родился ' + put))
    if answer == put_year: # Правильный ответ 1952
        reply += 1
    else:
        rereply += 1

    answer = int(input('В каком году родился ' + lom))
    if answer == lom_year: # Правильный ответ 1711
        reply += 1
    else:
        rereply += 1

    percent = (reply * 100) / 5
    repercent = (rereply * 100) / 5
    print('количество правильных ответов = ' + str(reply))
    print('количество неправильных ответов = ' + str(rereply))
    print('процент правильных ответов = ' + str(percent))
    print('процент неправильных ответов = ' + str(repercent))


    answer = input('Хотите ли вы начать игру заного ?') # Здесь не понял как зациклить последний вопрос если ответ и не да и не нет
    if answer == 'да':
        i -= 1
    elif answer == 'нет':
        break
    else:
        break

    i += 1