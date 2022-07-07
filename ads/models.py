from django.core.validators import MinLengthValidator
from django.db import models

from categories.models import Category
from users.models import User


class Ad(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.TextField(validators=[MinLengthValidator(10)], null=False)
    price = models.FloatField()
    description = models.TextField(null=True)
    is_published = models.BooleanField()

    image = models.ImageField(upload_to='images/', null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-price']
