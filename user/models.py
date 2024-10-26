import re

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('manager', 'Manager'),
    )

    name = models.CharField(max_length=155, default="User Name")
    password = models.CharField(max_length=155)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=122, default="User Phone")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"User name is {self.name}"

    @staticmethod
    def validate_data(request, data):
        if not re.search(r"\w+.?\w+.?.?@\w*\.\w+", data.get("email", "")):
            messages.error(request, "Wrong email")
            data["email"] = "basicemail@gmail.com"

        if not re.search(r"\d{7,10}", data.get("phone", "")):
            messages.error(request, "Not correct phone format")
            data["phone"] = "1111111"

        return data
