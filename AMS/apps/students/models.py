from django.db import models
from apps.curriculum.models import StudyGroup

class Student(models.Model):
    full_name = models.CharField("ФИО студента", max_length=150)
    student_card = models.CharField("Номер зачётки", max_length=30, unique=True)
    group = models.ForeignKey(StudyGroup, on_delete=models.PROTECT, related_name="students", verbose_name="Группа")
    email = models.EmailField("Email", blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.group.name})"
