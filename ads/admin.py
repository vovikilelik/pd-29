from django.contrib import admin

# Register your models here.
from ads.models import Ad, Category

admin.site.register(Ad)
admin.site.register(Category)
