status_note = ('выполняется','готово','просрочено')
i = 0
status = status_note[i]
print('Текущий статус заметки - "выполняется"')
print('Обновите статус заметки(либо Выполняется, Готово, Просрочено), (либо в формате 1, 2, 3)')
while True:
    status_change = input()
    if status_change.lower() in status_note:
        status = status_change
        print('Статус обновлен -',status)
        break

    else:
        if len(status_change) == 1:
            if status_change == '1' or '2' or '3':
                status_change = int(status_change)
                status = status_note[status_change - 1]
                print('Статус обновлен -',status)
                break
        else:
            print('не верно задан формат статуса, повторите попытку')
