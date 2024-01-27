import datetime as dt
from datetime import datetime
import random
import re


#                                      домашне завдання №1                        #   

# def get_days_from_today(date):
#     now = datetime.today()
#     try:
#         date = datetime.strptime(date,"%Y-%m-%d")
#     except Exception:
#         return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'"
    
#     difference = date - now
#     difference = int(difference.days)+1
#     return difference

# get_days_from_today()

#                                      Домашне завдання №2                        #

# def get_numbers_ticket(min, max, quantity=6):   
#     try: 
#         min >= 1 and max <= 1000
#         lottery_list = random.sample(range(min, max), quantity)
#         lottery_list.sort()
#         return lottery_list
#     except Exception:
#         return []
# get_numbers_ticket(1,20,6)

        

#                                      Домашне завдання №3                        #

# user_phone=[
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]
# def normalize_phone(phone_number):
#     p1=r"[\d\+]+"
#     phone_number=''.join(re.findall(p1,phone_number))
#     if len(phone_number)==10:
#         phone_number='+38'+phone_number
#     elif len(phone_number)==12:
#         phone_number='+'+phone_number
#     return phone_number

# for phone in user_phone:
#     print(normalize_phone(phone))

# normalize_phone(phone)

# #                                      Домашне завдання №4                        #


# users = [
#     {"name": "John Doe", "birthday": "1985.01.27"},
#     {"name": "Jane Smith", "birthday": "1990.01.28"}
# ]

# def get_upcoming_birthdays(users=None):
#     tdate=datetime.today().date()
#     birthdays=[]
#     for user in users:
#         bdate=user["birthday"] 
#         bdate=str(tdate.year)+bdate[4:]
#         bdate=datetime.strptime(bdate, "%Y.%m.%d").date()
#         week_day=bdate.isoweekday() 
#         days_between=(bdate-tdate).days 
#         if 0<=days_between<7:
#             if week_day<6:
#                 birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")}) 
#             else:
#                 if (bdate+dt.timedelta(days=1)).weekday()==0:
#                     birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
#                 elif (bdate+dt.timedelta(days=2)).weekday()==0:
#                     birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
#     return birthdays

# print(get_upcoming_birthdays(users))



    






