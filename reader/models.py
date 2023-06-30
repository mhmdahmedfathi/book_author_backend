from user.models import User

class Reader(User):
    # This is required for the custom user model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    role = 'reader'

    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.is_admin