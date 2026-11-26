from django.db import models

class StudyGroup(models.Model):
    name = models.CharField("Название группы", max_length=50, unique=True)
    course = models.PositiveIntegerField("Курс", default=2)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField("Дисциплина", max_length=150)
    hours = models.PositiveIntegerField("Количество часов", default=36)

    def __str__(self):
        return self.name
