from django.db import models
from django.conf import settings
from apps.students.models import Student
from apps.curriculum.models import Subject

class JournalRecord(models.Model):
    class Attendance(models.TextChoices):
        PRESENT = "present", "Присутствовал"
        ABSENT = "absent", "Отсутствовал (Н)"
        EXCUSED = "excused", "Уважительная причина"

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="records", verbose_name="Студент")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="records", verbose_name="Дисциплина")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Преподаватель")
    date = models.DateField("Дата занятия")
    grade = models.PositiveSmallIntegerField("Оценка (2-5)", null=True, blank=True)
    attendance = models.CharField("Посещаемость", max_length=20, choices=Attendance.choices, default=Attendance.PRESENT)
    comment = models.CharField("Примечание", max_length=255, blank=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name} ({self.date})"
