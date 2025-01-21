from datetime import datetime

current_date = input('Введите дату постановки задачи в формате дд.мм.гггг ')
issue_date = input('Введите дату сдачи задачи в формате дд.мм.гггг ')
date_obj_current = datetime.strptime(current_date, "%d.%m.%Y")
date_obj_issue = datetime.strptime(issue_date, "%d.%m.%Y")
print("Дата постановки задачи - ", date_obj_current.strftime("%d %b"))
print("Дата сдачи задачи - ", date_obj_issue.strftime("%d %b"))