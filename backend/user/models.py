from django.db import models
from django.contrib.auth.models import User

# Profile Model
# RDMS table which is extension of the base auth_user table created by django 
# add any additional field for user here 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=False, blank=False)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="media/profilePicture",default="/default.svg")

