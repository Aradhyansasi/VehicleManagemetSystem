from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone=models.CharField(max_length=14,default='+91-')
    options=(
        ('superAdmin','superAdmin'),
        ('admin','admin'),
        ('user', 'user')
    )
    role=models.CharField(max_length=15,choices=options,default='user')

    @property
    def is_superAdmin(self):
        return self.role=='superAdmin'
    def is_admin(self):
        return self.role=='admin'
    def is_user(self):
        return self.role=='user'
