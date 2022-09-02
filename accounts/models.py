from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class Profile(models.Model):
    role = models.CharField(max_length=50, blank=False, null=False, unique=True,)

    def __str__(self):
        return f"{self.role}"


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    # user.password = password # bad - do not do this

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, validators=[
        RegexValidator(regex=USERNAME_REGEX, message='Username must be alphanumeric or contain numbers',
                       code='invalid_username')],
                                unique=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email address')
    phone = models.CharField(max_length=20, unique=True, null=True, verbose_name='Telephone')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True, default='')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True
