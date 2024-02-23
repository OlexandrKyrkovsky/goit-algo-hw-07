from collections import UserDict
import re
import datetime as dt
from datetime import datetime as dtdt


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Номер телефону має містити 10 цифр.") 
        super().__init__(value)
        
class Birthday(Field):
    def __init__(self, value):
        try:
            patern=r'\d{2}\.\d{2}\.d{4}'
            if re.match(patern,value):
                self.value = dtdt.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
class Record:
    def __init__(self, name):
        self.name =Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self,phone):
        
        self.phones.append(Phone(phone))
        

    def remove_phone(self,phone):
        if phone in self.phones:
            self.phones.remove(phone)


    def edit_phone(self,phone_old,phone_new):
        for p in self.phones:
            if p.value == phone_old:
                p.value = phone_new
                break


    def find_phone(self,phone):
        if phone in self.phones:
            return phone
        
    def add_birthday(self,birthday):
        self.birthday=birthday
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):
    # реалізація класу
    book={}      
    def add_record(self,record):
        self.data[record.name.value]=record

    def find(self,name):
        return self.data.get(name)
		
    def delete(self,name):
        if name in self.data:
            del self.data[name]

    def birthdays(book):
        today_date=dtdt.today().date()
        birthdays=[]
        for user in book:
            birth_date=user['birthday']
            birth_date=str(today_date.year)+birth_date[:4]
            birth_date=dtdt.strptime(birth_date, "%d.%m.%Y").date()
            w_day=birth_date.isoweekday()
            days_difference=(birth_date-today_date).days
            if 0<=days_difference<7:
                if w_day<6:
                    birthdays.append({'name':user['name'],'birthday':birth_date.strftime("%d.%m.%Y")})
                else:
                    if (birth_date+dt.timedelta(days=1)).weekday()==0:
                        birthdays.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=1)).strftime("%d.%m.%Y")})
                    elif (birth_date+dt.timedelta(days=2)).weekday()==0: 
                        birthdays.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=2)).strftime("%d.%m.%Y")})     
        return birthdays

# # # Створення нової адресної книги
# book = AddressBook()

# #     # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday('25.02.1999')
# print(john_record)
# #     # Додавання запису John до адресної книги
# book.add_record(john_record)

# #     # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# #     # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# #     # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# #     # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # #     # Видалення запису Jane
# # book.delete("Jane")
# print(book.birthdays)

