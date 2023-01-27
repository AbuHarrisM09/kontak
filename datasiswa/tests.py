from django.test import TestCase
from .models import Datasiswa

class StudentTestCase(TestCase):
    def setUp(self):
        # create test data
        self.student = Datasiswa.objects.create(
            nama='John Doe',
            email='john@gmail.com',
            hp='08123456789',
            alamat='New York',
            jenis_kelamin='L',
            tempat_lahir='Bandung'
            
            )

    def test_create_student(self):
        # test creating a new student
        new_student = Datasiswa.objects.create(nama='John Doe',
            email='john@gmail.com',
            hp='08123456789',
            alamat='New York',
            jenis_kelamin='L',
            tempat_lahir='Bandung')
        self.assertEqual(Datasiswa.objects.count(), 2)
        self.assertEqual(new_student.name, 'Jane Smith')

    def test_read_student(self):
        # test reading a student
        student = Datasiswa().objects.get(id=self.student.id)
        self.assertEqual(student.name, 'John Doe')

    def test_update_student(self):
        # test updating a student
        self.student.name = 'John Smith'
        self.student.save()
        student = Datasiswa().objects.get(id=self.student.id)
        self.assertEqual(student.name, 'John Smith')

    def test_delete_student(self):
        # test deleting a student
        self.student.delete()
        self.assertEqual(Datasiswa().objects.count(), 0)
