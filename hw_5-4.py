from hw_6 import AddressBook, Record
# from birthday import birthdays

book=AddressBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone in 10-digit addplease."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
    
@input_error
def add_contact(args, book):
        name, phone = args
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."

@input_error
def change_contact(args, book):
    if args[0] in book.keys():
        add_contact(args, book)
        return 'Contact changed'
    else:
        raise(KeyError)

@input_error
def show_phone(args, book):
    return book[args[0]]

@input_error
def show_all(book):
    s=''
    for key in book:
        s+=(f"{key:10} : {book[key]}\n")
    return s

@input_error
def add_birthday(args, book):
    name,birthday=args
    user_record = book.get(name)
    user_record.add_birthday(birthday)
    # user_record.birthday = birthday
    # record = Record(name)
    # record.add_birthday(birthday)
    # book.add_record(record)
    return "Birthday added"
    

@input_error
def show_birthday(args, book):
    return book[args[0]]

@input_error
def birthdays(book):
    result_dict = book.birthdays()
    congratulation_list = []
    for user in result_dict:
        congratulation_list.append(f'Congratualation date: {user['birthday']} Name: {user['name']}')
    return '\n'.join(congratulation_list)


def main():
    book=AddressBook()
    # record = Record('Edd')
    # record.add_phone('1234567890')
    # record.add_birthday('25.02.2000')
    # book.add_record(record)
    # print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args,book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args,book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
