from django.contrib import admin
from .models import Publisher, Newsletter, Article


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Newsletter)
admin.site.register(Article)