from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.AutoField(null=False, blank=False, primary_key=True)
    category_name = models.CharField(null=False, blank=False, max_length=25)
    video = models.FileField(upload_to="uploads/", blank=False, null=False)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.category_name


class Questionnaire(models.Model):
    id = models.AutoField(null=False, blank=False, primary_key=True)
    question = models.TextField(null=False, blank=False, max_length=500)
    answer = models.TextField(null=False, blank=False, max_length=500)
    choice1 = models.TextField(null=False, blank=False, max_length=500)
    choice2 = models.TextField(null=False, blank=False, max_length=500)
    choice3 = models.TextField(null=False, blank=False, max_length=500)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Questionnaire"
        verbose_name = "Questionnaire"

    def __str__(self):
        return self.question

