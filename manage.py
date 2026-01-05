#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insurance_project.settings') # <--- CHANGE 'insurance_project' to your folder name!
django.setup()

from django.contrib.auth.models import User

def create_user():
    USERNAME = 'postgres'
    PASSWORD = '123456789'
    EMAIL = 'leongmr0824@gmail.com'

    if User.objects.filter(username=USERNAME).exists():
        print("Superuser already exists. Skipping...")
    else:
        User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
        print(f"Superuser {USERNAME} created successfully!")

if __name__ == "__main__":
    create_user()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insurance_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
