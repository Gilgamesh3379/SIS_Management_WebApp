# # tests.py
#
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import CourseProgram
# from .serializers import CourseProgramSerializer
#
#
# class CourseProgramViewSetTests(APITestCase):
#
#     def setUp(self):
#         # Create sample data for CourseProgram
#         self.course_program_1 = CourseProgram.objects.create(name="Program 1", description="Description 1")
#         self.course_program_2 = CourseProgram.objects.create(name="Program 2", description="Description 2")
#
#     def test_list_course_programs(self):
#         url = reverse('courseprogram-list')
#         response = self.client.get(url)
#         programs = CourseProgram.objects.all()
#         serializer = CourseProgramSerializer(programs, many=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
#
#     def test_create_course_program(self):
#         url = reverse('courseprogram-list')
#         data = {
#             'name': 'Program 3',
#             'description': 'Description 3'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(CourseProgram.objects.count(), 3)
#         self.assertEqual(CourseProgram.objects.get(id=response.data['id']).name, 'Program 3')
#
#     def test_retrieve_course_program(self):
#         url = reverse('courseprogram-detail', args=[self.course_program_1.id])
#         response = self.client.get(url)
#         serializer = CourseProgramSerializer(self.course_program_1)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
#
#     def test_update_course_program(self):
#         url = reverse('courseprogram-detail', args=[self.course_program_1.id])
#         data = {
#             'name': 'Updated Program 1',
#             'description': 'Updated Description 1'
#         }
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.course_program_1.refresh_from_db()
#         self.assertEqual(self.course_program_1.name, 'Updated Program 1')
#         self.assertEqual(self.course_program_1.description, 'Updated Description 1')
#
#     def test_delete_course_program(self):
#         url = reverse('courseprogram-detail', args=[self.course_program_1.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(CourseProgram.objects.count(), 1)
#
#
# # class TuitionViewSetTests(APITestCase):
# #
# #     def setUp(self):
# #         # Create sample data for Tuition
# #         self.tuition_1 = Tuition.objects.create(amount=1000, due_date="2024-12-31")
# #         self.tuition_2 = Tuition.objects.create(amount=2000, due_date="2024-11-30")
# #
# #     def test_list_tuitions(self):
# #         url = reverse('tuition-list')
# #         response = self.client.get(url)
# #         tuitions = Tuition.objects.all()
# #         serializer = TuitionSerializer(tuitions, many=True)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data, serializer.data)
# #
# #     def test_create_tuition(self):
# #         url = reverse('tuition-list')
# #         data = {
# #             'amount': 3000,
# #             'due_date': '2024-10-31'
# #         }
# #         response = self.client.post(url, data, format='json')
# #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# #         self.assertEqual(Tuition.objects.count(), 3)
# #         self.assertEqual(Tuition.objects.get(id=response.data['id']).amount, 3000)
# #
# #     def test_retrieve_tuition(self):
# #         url = reverse('tuition-detail', args=[self.tuition_1.id])
# #         response = self.client.get(url)
# #         serializer = TuitionSerializer(self.tuition_1)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data, serializer.data)
# #
# #     def test_update_tuition(self):
# #         url = reverse('tuition-detail', args=[self.tuition_1.id])
# #         data = {
# #             'amount': 1500,
# #             'due_date': '2024-09-30'
# #         }
# #         response = self.client.put(url, data, format='json')
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.tuition_1.refresh_from_db()
# #         self.assertEqual(self.tuition_1.amount, 1500)
# #         self.assertEqual(self.tuition_1.due_date, '2024-09-30')
# #
# #     def test_delete_tuition(self):
# #         url = reverse('tuition-detail', args=[self.tuition_1.id])
# #         response = self.client.delete(url)
# #         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
# #         self.assertEqual(Tuition.objects.count(), 1)
