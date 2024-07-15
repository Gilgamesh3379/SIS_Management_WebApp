from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import CourseProgram, StudentProfile, LecturerProfile
from .serializers import CourseProgramSerializer, StudentProfileSerializer, LecturerProfileSerializer

class CourseProgramViewSetTests(APITestCase):

    def setUp(self):
        # Create sample data for CourseProgram
        self.course_program_1 = CourseProgram.objects.create(name="Program 1", description="Description 1")
        self.course_program_2 = CourseProgram.objects.create(name="Program 2", description="Description 2")

    def test_list_course_programs(self):
        url = reverse('courseprogram-list')
        response = self.client.get(url)
        programs = CourseProgram.objects.all()
        serializer = CourseProgramSerializer(programs, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_course_program(self):
        url = reverse('courseprogram-list')
        data = {
            'name': 'Program 3',
            'description': 'Description 3'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CourseProgram.objects.count(), 3)
        self.assertEqual(CourseProgram.objects.get(id=response.data['id']).name, 'Program 3')

    def test_retrieve_course_program(self):
        url = reverse('courseprogram-detail', args=[self.course_program_1.id])
        response = self.client.get(url)
        serializer = CourseProgramSerializer(self.course_program_1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_course_program(self):
        url = reverse('courseprogram-detail', args=[self.course_program_1.id])
        data = {
            'name': 'Updated Program 1',
            'description': 'Updated Description 1'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course_program_1.refresh_from_db()
        self.assertEqual(self.course_program_1.name, 'Updated Program 1')
        self.assertEqual(self.course_program_1.description, 'Updated Description 1')

    def test_delete_course_program(self):
        url = reverse('courseprogram-detail', args=[self.course_program_1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CourseProgram.objects.count(), 1)


class StudentProfileViewSetTests(APITestCase):

    def setUp(self):
        # Create sample data for StudentProfile
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.course_program = CourseProgram.objects.create(name="Program 1", description="Description 1")
        self.student_profile = StudentProfile.objects.create(
            user=self.user,
            name="Student 1",
            email="student1@example.com",
            phone="1234567890",
            address="123 Main St",
            mother_name="Mother 1",
            father_name="Father 1"
        )
        self.student_profile.courses.add(self.course_program)

    def test_list_student_profiles(self):
        url = reverse('studentprofile-list')
        response = self.client.get(url)
        students = StudentProfile.objects.all()
        serializer = StudentProfileSerializer(students, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_student_profile(self):
        url = reverse('studentprofile-list')
        data = {
            'user': self.user.id,
            'name': 'Student 2',
            'email': 'student2@example.com',
            'phone': '0987654321',
            'address': '456 Another St',
            'mother_name': 'Mother 2',
            'father_name': 'Father 2',
            'courses': [self.course_program.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StudentProfile.objects.count(), 2)
        self.assertEqual(StudentProfile.objects.get(id=response.data['id']).name, 'Student 2')

    def test_retrieve_student_profile(self):
        url = reverse('studentprofile-detail', args=[self.student_profile.id])
        response = self.client.get(url)
        serializer = StudentProfileSerializer(self.student_profile)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_student_profile(self):
        url = reverse('studentprofile-detail', args=[self.student_profile.id])
        data = {
            'user': self.user.id,
            'name': 'Updated Student 1',
            'email': 'updated_student1@example.com',
            'phone': '1234567890',
            'address': '123 Main St',
            'mother_name': 'Updated Mother 1',
            'father_name': 'Updated Father 1',
            'courses': [self.course_program.id]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student_profile.refresh_from_db()
        self.assertEqual(self.student_profile.name, 'Updated Student 1')
        self.assertEqual(self.student_profile.email, 'updated_student1@example.com')

    def test_delete_student_profile(self):
        url = reverse('studentprofile-detail', args=[self.student_profile.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(StudentProfile.objects.count(), 0)


class LecturerProfileViewSetTests(APITestCase):

    def setUp(self):
        # Create sample data for LecturerProfile
        self.user = User.objects.create_user(username='testlecturer', password='testpass')
        self.course_program = CourseProgram.objects.create(name="Program 1", description="Description 1")
        self.lecturer_profile = LecturerProfile.objects.create(
            user=self.user,
            name="Lecturer 1",
            email="lecturer1@example.com",
            phone="1234567890",
            address="123 Main St",
            program=self.course_program
        )

    def test_list_lecturer_profiles(self):
        url = reverse('lecturerprofile-list')
        response = self.client.get(url)
        lecturers = LecturerProfile.objects.all()
        serializer = LecturerProfileSerializer(lecturers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_lecturer_profile(self):
        url = reverse('lecturerprofile-list')
        data = {
            'user': self.user.id,
            'name': 'Lecturer 2',
            'email': 'lecturer2@example.com',
            'phone': '0987654321',
            'address': '456 Another St',
            'program': self.course_program.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LecturerProfile.objects.count(), 2)
        self.assertEqual(LecturerProfile.objects.get(id=response.data['id']).name, 'Lecturer 2')

    def test_retrieve_lecturer_profile(self):
        url = reverse('lecturerprofile-detail', args=[self.lecturer_profile.id])
        response = self.client.get(url)
        serializer = LecturerProfileSerializer(self.lecturer_profile)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_lecturer_profile(self):
        url = reverse('lecturerprofile-detail', args=[self.lecturer_profile.id])
        data = {
            'user': self.user.id,
            'name': 'Updated Lecturer 1',
            'email': 'updated_lecturer1@example.com',
            'phone': '1234567890',
            'address': '123 Main St',
            'program': self.course_program.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lecturer_profile.refresh_from_db()
        self.assertEqual(self.lecturer_profile.name, 'Updated Lecturer 1')
        self.assertEqual(self.lecturer_profile.email, 'updated_lecturer1@example.com')

    def test_delete_lecturer_profile(self):
        url = reverse('lecturerprofile-detail', args=[self.lecturer_profile.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(LecturerProfile.objects.count(), 0)
