from django.contrib import admin
from .models import Category, Items, Tag

# Register your models here.
admin.site.register(Items)
admin.site.register(Category)
admin.site.register(Tag)
