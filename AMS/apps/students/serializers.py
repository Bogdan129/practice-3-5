from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source="group.name", read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "full_name",
            "student_card",
            "group",
            "group_name",
            "email",
        ]

    def validate_student_card(self, value):
        qs = Student.objects.filter(student_card=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Студент с таким номером зачётной книжки уже существует.")
        return value
