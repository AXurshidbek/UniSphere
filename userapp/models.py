from django.db import models
from django.contrib.auth.models import AbstractUser
ROLES=(('Student', 'Student'),
       ('Center', 'Center'))


class User(AbstractUser):
    last_name = None
    picture = models.FileField()
    phone_number = models.CharField(max_length=17, null=True, blank=True)
    role = models.CharField(max_length=15, choices=ROLES)

    def save(self, *args, **kwargs):
        # If username is not set and phone_number is set, set username to phone_number
        if not self.username and self.phone_number:
            self.username = self.phone_number
        super().save(*args, **kwargs)



