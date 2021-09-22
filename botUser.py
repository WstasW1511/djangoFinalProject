from random import randint
import requests


class UserBot:
    def __init__(self):
        self.phone = self.number(10)
        self.password = self.password(6)
        self.is_active = self.is_active()
        self.is_staff = self.is_staff()

    def getInfo(self):
        print(f'Phone: {self.phone}, Password: {self.password}, Staff: {self.is_staff}, Activ: {self.is_active}')

    def number(self, n):
        start = 10 ** (n - 1)
        end = (10 ** n) - 1
        return randint(start, end)

    def password(self, n):
        start = 10 ** (n - 1)
        end = (10 ** n) - 1
        return randint(start, end)

    def is_staff(self):
        choise = randint(0, 1)
        if choise == 0:
            is_staff = False
        elif choise == 1:
            is_staff = True
        return is_staff

    def is_active(self):
        choise = randint(0, 1)
        if choise == 0:
            is_active = False
        elif choise == 1:
            is_active = True
        return is_active


howUsersCreate = int(input('Введите количество юзеров которое нужно создать: '))
mass = []
for i in range(howUsersCreate):
    user = UserBot()
    try:
        r = requests.post('http://127.0.0.1:8000/users/registration/', data=({'phone': user.phone,
                                                                         'password': user.password,
                                                                              'is_staff': user.is_staff(),
                                                                              'is_active()': user.is_active(),
                                                                              'kind': 'User1'
                                                                              }))
        mass.append(user)
    except:
        print('dont created')

for i in mass:
    print(i.getInfo())
