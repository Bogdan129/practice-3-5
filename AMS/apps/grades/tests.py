from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.curriculum.models import StudyGroup, Subject
from apps.students.models import Student
from apps.grades.models import JournalRecord

User = get_user_model()


class ElectronicJournalTests(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username="teacher1",
            password="testpassword123",
            full_name="Иванов Иван Иванович",
            role="teacher",
        )
        self.group = StudyGroup.objects.create(name="ИСП-231", course=2)
        self.subject = Subject.objects.create(name="Разработка ПО", hours=72)
        self.student = Student.objects.create(
            full_name="Кудашев Богдан Сергеевич",
            student_card="231-001",
            group=self.group,
        )
        self.client = APIClient()

    def test_student_and_group_creation(self):
        self.assertEqual(self.student.group.name, "ИСП-231")

    def test_journal_record_creation(self):
        record = JournalRecord.objects.create(
            student=self.student,
            subject=self.subject,
            teacher=self.teacher,
            date=date.today(),
            grade=5,
            attendance=JournalRecord.Attendance.PRESENT,
        )
        self.assertEqual(record.grade, 5)
        self.assertEqual(JournalRecord.objects.count(), 1)

    def test_jwt_login_success(self):
        response = self.client.post(
            "/api/auth/login/",
            {"username": "teacher1", "password": "testpassword123"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_admin_redirect_for_anonymous(self):
        response = self.client.get("/admin/", follow=False)
        self.assertEqual(response.status_code, 302)
