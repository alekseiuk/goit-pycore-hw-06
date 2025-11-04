from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    
    def __init__(self, phone_number):
        if self.validate(phone_number):
            self.value = phone_number
        else:
            raise ValueError(f'Invalid phone number: {phone_number}. Must be 10 digits.')

    @staticmethod
    def validate(number):
        return number.isdigit() and len(number) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        exists = self.find_phone(phone_number)
        if not exists:
            try:
                phone = Phone(phone_number)
                self.phones.append(phone)
            except ValueError as error:
                print(f'{error}')
    
    def edit_phone(self, old_phone, new_phone):
        old_phone_exists = self.find_phone(old_phone)
        if old_phone_exists:
            index = self.phones.index(old_phone_exists)
            try:
                new_phone = Phone(new_phone)
                self.phones[index] = new_phone
            except ValueError as error:
                print(f'{error}')

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def find_record(self, name):
        for n in self.data:
            if n.value == name:
                return self.data[n]
        return None

    def delete_record(self, name):
        record = self.find_record(name)
        if record:
            del self.data[record.name]

    def print_book(self):
        for name, record in self.data.items():
            print(record)



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
book.print_book()

# Знаходження та редагування телефону для John
john = book.find_record("John")
john.edit_phone("1234567890", "111222333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete_record("Jane")
book.print_book()