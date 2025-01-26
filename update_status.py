status_note = ('выполняется','готово','просрочено')
status = input('Введите статус заметки в формете "выполняется","готово","просрочено" - ')
if status in status_note:
    print('status zametki izmenen na', status)
else:
    print('ne verno zadano znachenie statusa')
