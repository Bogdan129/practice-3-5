from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Администратор"
        TEACHER = "teacher", "Преподаватель"
        CURATOR = "curator", "Куратор группы"

    full_name = models.CharField("ФИО", max_length=255, blank=True)
    role = models.CharField("Роль", max_length=20, choices=Role.choices, default=Role.TEACHER)

    def __str__(self):
        return f"{self.full_name or self.username} ({self.get_role_display()})"
