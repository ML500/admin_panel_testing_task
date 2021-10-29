from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Defines user creation fields and manages to save user
    """

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.create_user(
            password=password,
            username=username
        )
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.create_user(
            password=password,
            username=username
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    """
    Creates a customized database table for user using customized user manager
    """
    user_id = models.AutoField(primary_key=True)
    username = models.CharField('username',
                                max_length=150,
                                unique=True,
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                },
                                )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        # db
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'
