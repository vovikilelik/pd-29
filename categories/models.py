from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.TextField()
    slug = models.SlugField(unique=True, max_length=10, null=False, validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
