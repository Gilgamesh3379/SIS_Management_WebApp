# tests/test_models.py
import pytest
from django.utils import timezone
from decimal import Decimal
from .models import CourseProgram

@pytest.mark.django_db
def test_course_program_creation():
    course_program = CourseProgram.objects.create(
        name="Test Course",
        description="A course for testing purposes",
        duration=12,
        tuition_fee=Decimal('1500.00'),
    )

    assert course_program.name == "Test Course"
    assert course_program.description == "A course for testing purposes"
    assert course_program.duration == 12
    assert course_program.tuition_fee == Decimal('1500.00')
    assert course_program.created_at <= timezone.now()
    assert course_program.updated_at <= timezone.now()

@pytest.mark.django_db
def test_course_program_str():
    course_program = CourseProgram.objects.create(
        name="Test Course",
        description="A course for testing purposes",
    )
    assert str(course_program) == "Test Course"

@pytest.mark.django_db
def test_course_program_defaults():
    course_program = CourseProgram.objects.create(
        name="Default Course",
        description="A course with default values",
    )
    assert course_program.duration == 6
    assert course_program.tuition_fee is None
