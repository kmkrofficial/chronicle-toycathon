from django.contrib import admin
from .models import Questionnaire, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Questionnaire)
