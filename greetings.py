username = 'Имя пользователя'
title = 'Заголовок заметки'
content = 'Описание заметки'
status = 'Статус'
day_start = 20
month_start = 1
year_start = 2025
created_date = day_start, month_start, year_start
day_end = 21
month_end = 1
year_end = 2025
issue_date = day_end, month_end, year_end
print('Имя пользователя',username)
print('Заголовок заметки', title)
print('Описание заметки', content)
print('Статус заметки', status)
print('Дата создания заметки', end=' ')
print(day_start, month_start, year_start, sep='-')
print('Дата истечения заметки(дедлайн)', end=' ')
print(day_end,month_end,year_end, sep='-')
