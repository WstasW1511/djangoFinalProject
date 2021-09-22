from random import randint
import requests


def phone(n):
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return randint(start, end)

def is_staff():
    choise = randint(0, 1)
    if choise == 0:
        is_staff = False
    elif choise == 1:
        is_staff = True
    return is_staff

def is_active():
    choise =randint(0,1)
    if choise == 0:
        is_active = False
    elif choise == 1:
        is_active = True
    return is_active


class UserBot:
    def __init__(self, phone, is_staff, is_active, password):
        self.phone = phone
        self.password = password
        self.is_active = is_active
        self.is_staff = is_staff

    def getInfo(self):
        print(f'Phone: {self.phone}, Password: {self.password}')

    def number(n):
        start = 10 ** (n - 1)
        end = (10 ** n) - 1
        return randint(start, end)


howUsersCreate = int(input('Введите количество юзеров которое нужно создать: '))
mass = []
for i in range(howUsersCreate):
    user = UserBot(phone=phone(10), is_staff=is_staff(), is_active=is_active(), password=phone(6))
    try:
        r = requests.post('http://127.0.0.1:8000/users/registration/', data=({'phone': user.phone,
                                                                         'password': user.password,
                                                                              'is_staff': is_staff(),
                                                                              'is_active()':is_active(),
                                                                              'kind': 'User1'
                                                                              }))
        mass.append(user)
    except:
        print('dont created')

for i in mass:
    print(i.getInfo())
