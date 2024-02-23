import datetime as dt
from datetime import datetime as dtdt

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def birthdays(book):
    today_date=dtdt.today().date()
    birthdays=[]
    for user in book:
        birth_date=user['birthday']
        birth_date=str(today_date.year)+birth_date[4:]
        birth_date=dtdt.strptime(birth_date, "%Y.%m.%d").date()
        w_day=birth_date.isoweekday()
        days_difference=(birth_date-today_date).days
        if 0<=days_difference<7:
            if w_day<6:
                birthdays.append({'name':user['name'],'birthday':birth_date.strftime("%Y.%m.%d")})
            else:
                if (birth_date+dt.timedelta(days=1)).weekday()==0:
                    birthdays.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (birth_date+dt.timedelta(days=2)).weekday()==0: 
                    birthdays.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=2)).strftime("%Y.%m.%d")})     
    return birthdays
    

# upcoming_birthdays=birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)