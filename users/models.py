from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

