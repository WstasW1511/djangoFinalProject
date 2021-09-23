import random
from random import randint, choice
import requests
from string import ascii_letters
from datetime import datetime
from string import digits


class UserBot:
    def __init__(self):
        self.phone = self.number(10)
        self.password = self.password(8)
        self.is_active = self.is_active()
        self.is_staff = self.is_staff()

    def number(self, n):
        number = ''.join(choice(digits) for i in range(n))
        return number

    def password(self, n):
        password = ''.join(choice(digits) for i in range(n))
        return password

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

    def getInfo(self):
        print(f'Phone: {self.phone}, Password: {self.password}, Staff: {self.is_staff}, Activ: {self.is_active}')


howUsersCreate = int(input('Введите количество юзеров которое нужно создать: '))
start_time = datetime.now()
for i in range(howUsersCreate):
    user = UserBot()
    try:
        r = requests.post('http://127.0.0.1:8000/users/registration/', data=({'phone': user.phone,
                                                                         'password': user.password,
                                                                              'is_staff': user.is_staff,
                                                                              'is_active': user.is_active,
                                                                              'kind': 'User1'
                                                                              }))
        log_in = requests.post('http://127.0.0.1:8000/users/login/', data=({
                                                                            'phone': user.phone,
                                                                            'password': user.password
                                                                            }))
        tokens = log_in.json()
        actoken = tokens['tokens']['access']
        views = ['Blog', 'News', 'Advertising']
        view = random.choice(views)
        text = ''.join(choice(ascii_letters) for i in range(10))
        post = requests.post('http://127.0.0.1:8000/posts/list/', headers={'Authorization': 'Bearer {}'.format(actoken)},
                                                                data={
                                                                'text': text,
                                                                'view': view
                                                                    })
    except:
        print("Don't login!")
print('Created', howUsersCreate, 'posts')
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
