from random import randint

import pytest
from django.contrib.auth.models import User
from django.test import Client

from shopping_lists.models import Space, Fridge, ShoppingList


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def set_up():
    users = []
    for i in range(3):
        u = User.objects.create(username=f'User{i}')
        users.append(u)


    for user in users:
        for i in range(randint(2, 6)):
            space = Space.objects.create(name=str(i))
            space.users.add(user)

            for j in range(randint(3, 7)):
                fridge = Fridge.objects.create(name=str(i + 100 * j), space=space)

                for k in range(randint(2, 8)):
                    ShoppingList.objects.create(name=str(i + j + k), fridge=fridge)

    return users


@pytest.fixture
def user_without_space():
    password = 'password'
    username = 'username'
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    return username, password
