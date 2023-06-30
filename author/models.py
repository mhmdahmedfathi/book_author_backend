from django.db import models
from user.models import User
# Create your models here.
class Author(User):
    # This is required for the custom user model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    role = 'author'

    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.is_admin