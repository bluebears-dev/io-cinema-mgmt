from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

PHONE_NUMBER_REGEX = r'(\d{2} ?\d{3}(?: ?\d{2}){2})|' \
                     r'(\d{3}(?: \d{3}){2})'
"""
Matches number delimited space in three different formats:
  12 345 67 89
  123 456 789
  123456789
"""


class UserProfile(models.Model):
  """
  User profile containing non-auth data
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=12, validators=[
    RegexValidator(
      regex=PHONE_NUMBER_REGEX,
      message="Enter valid phone number (may contain spaces)"
    )
  ])
