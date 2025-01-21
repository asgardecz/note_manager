from dateutil import parser
current_date = input('Введите дату постановки задания - ')
issue_date = input('Введите дату сдачи задания - ')
current_date_obj = parser.parse(current_date)
issue_date_obj = parser.parse(issue_date)
print('Дата постановки задания - ', current_date_obj.strftime("%d. %b"))
print('Дата сдачи задания - ', issue_date_obj.strftime("%d. %b"))

