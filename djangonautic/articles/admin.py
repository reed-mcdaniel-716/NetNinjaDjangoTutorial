from django.contrib import admin
# importing Article model from models.py
from .models import Article

# Register your models here.
admin.site.register(Article)
