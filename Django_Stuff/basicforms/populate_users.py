import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basicforms.settings')

import django
django.setup()

# Fake Pop Script
import random
from usersapp.models import User
from faker import Faker

fakegen = Faker()


def populate(number_of_times = 5):
    for entry in range(number_of_times):

        fake_name = fakegen.name().split()

        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]


if __name__ == '__main__':
    print('Populating User model!')
    populate(number_of_times=20)
    print('Populated Successfully!')

