# tests/test_models.py
from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from .models import CourseProgram

class CourseProgramTestCase(TestCase):

    def test_course_program_creation(self):
        course_program = CourseProgram.objects.create(
            name="Test Course",
            description="A course for testing purposes",
            duration=12,
            tuition_fee=Decimal('1500.00'),
        )

        self.assertEqual(course_program.name, "Test Course")
        self.assertEqual(course_program.description, "A course for testing purposes")
        self.assertEqual(course_program.duration, 12)
        self.assertEqual(course_program.tuition_fee, Decimal('1500.00'))
        self.assertLessEqual(course_program.created_at, timezone.now())
        self.assertLessEqual(course_program.updated_at, timezone.now())

    def test_course_program_str(self):
        course_program = CourseProgram.objects.create(
            name="Test Course",
            description="A course for testing purposes",
        )
        self.assertEqual(str(course_program), "Test Course")

    def test_course_program_defaults(self):
        course_program = CourseProgram.objects.create(
            name="Default Course",
            description="A course with default values",
        )
        self.assertEqual(course_program.duration, 6)
        self.assertIsNone(course_program.tuition_fee)
