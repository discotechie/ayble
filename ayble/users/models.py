from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.constants import SEX_CHOICES, ETHNICITY_CHOICES
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sex_at_birth = models.CharField(
        null=True,
        max_length=1,
        choices=SEX_CHOICES,
    )
    ethnicity = models.CharField(
        null=True,
        max_length=50, 
        choices=ETHNICITY_CHOICES,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email