from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.db.models import Q


# Create your models here.

class UserManager(BaseUserManager):
    """
    Creates and saves a User with the given data.
    """
    def create(self, **kwargs):
        if not kwargs.get('username'):
            raise ValidationError("Username not given")

        user = self.model(**kwargs)
        user.set_password(kwargs.get('password'))
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username, and password.
        """
        user = self.create(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = 'CUSTOMER', 'customer'
        STANDARD = 'STD', 'base employee'
        MANAGER = 'MGR' , 'manager'
        SR_MANAGER = 'SRMGR', 'senior manager'
        PRESIDENT = 'PRES', 'president'

    
    # EMAIL_FIELD = "email"
    # USERNAME_FIELD = "username"
    


    phone_number = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=25, choices=Role.choices, null=False, blank=False)
    manager_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    objects = UserManager()
    # REQUIRED_FIELDS = ["role"]


    def __str__(self) -> str:
        return self.username




class CustomerManager(UserManager):
    def get_queryset(self):
        result = super().get_queryset()
        return result.filter(Q(role=User.Role.CUSTOMER))
    
class Customer(User):
    class Meta:
        proxy = True

    objects = CustomerManager()

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.role = User.Role.CUSTOMER
        return super().save(*args, **kwargs)


class StaffManager(UserManager):
    def get_queryset(self):
        result = super().get_queryset()
        return result.filter(~Q(role=User.Role.CUSTOMER))


class Staff(User):
    class Meta:
        proxy = True


    objects = StaffManager()

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.is_staff = True
            self.role = User.Role.STANDARD
        return super().save(*args, **kwargs)


    


    
