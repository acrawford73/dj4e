from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,
        help_text='Enter a make (e.g. Honda)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")])
    def get_absolute_url(self):
        return reverse('make-list')
    def __str__(self):
        return str(self.name)

class Autos(models.Model):
    nickname = models.CharField(max_length=50, default="", null=False, blank=False,
        validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")])
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
    mileage = models.PositiveIntegerField(default=0, null=True, blank=True)
    comments = models.CharField(max_length=300, default="", null=True, blank=True)
    def get_absolute_url(self):
        return reverse('auto-list')
    def __str__(self):
        return self.nickname
