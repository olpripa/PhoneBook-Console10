from collections import UserDict


class Field:
    def __init__(self, value):
        self.name = value


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, value) -> None:
        self.phone = value
        # self.sanitize()

    def __setattr__(self, name, value):
        self.__dict__[name] = self.sanitize(value)

    def __eq__(self, other):
        if hasattr(other, 'phone'):
            return self.phone == other.phone
        return self.value == other


    def sanitize(self, phone):
        phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return phone


class Record(Field):

    def __init__(self, value, *phone):
        self.name = Name(value)
        self.phone = [*phone]

    # function add new Phone to Phone list of User

    def showphone(self):
        result = ''
        for v in self.phone:
            result += f'{v.phone} '
        result += '\n'
        return result

    def addphone(self, phone):  # phone --> object class Phone

        if phone in self.phone:
            return f'User {self.name.name} already exiting phone: {phone.phone}'
        else:
            self.phone.append(phone)
            return (f'Phone: {phone.phone} add to list of User {self.name.name}')

    # function  delete Phone from Phone list of User

    def delphone(self, phone):  # phone --> object class Phone

        if phone in self.phone:
            self.phone.remove(phone)
            print(
                f'Phone: {phone.phone} delete from list of User {self.name.name}')
        else:
            print(f'User {self.name.name} not have phone: {phone.phone}')

    # function edit Phone from Phone list of User
    def editphone(self, phone, new_phone):  # phone --> object class Phone

        if phone in self.phone:
            # self.phone.remove(phone)
            phone.phone = new_phone
            print(
                f'Phone: {phone.phone} change in list of User {self.name.name}')
        else:
            print(f'User {self.name.name} not have phone: {phone.phone}')


class AdressBook(UserDict):

    def add(self, record):
        # self[r.name] = r
        self.update({record.name.name: record})
