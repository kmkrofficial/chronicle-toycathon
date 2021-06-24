from django.contrib import admin
from .models import Questionnaire, Category, Score

# Register your models here.
admin.site.register(Category)
admin.site.register(Questionnaire)
admin.site.register(Score)