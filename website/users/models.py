from django.db import models
from django.contrib.auth.models import User


# Class that inherits from the Model from Django
# CASCADE is one way delete - If user deleted, delete profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # This is how we want the Profile to be displayed
    def __str__(self):
        return f'{self.user.username} Profile'