from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from student.models import Person, Group, Subject, Course, Lesson


class PersonViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user.set_password('test_pass')
        self.user.save()

        self.client.login(username='test_user', password='test_pass')
        self.person = Person.objects.create(first_name='test_first', last_name='test_last', age=27)

    def test_create_student_endpoint(self):
        self.client.post(reverse('person-list'),
                         data={'first_name': 'test_second', 'last_name': 'test_last2', 'age': 17})
        self.assertEqual(Person.objects.count(), 2)
        student = Person.objects.all()[1]
        self.assertEqual(student.first_name, 'test_second')
        self.assertEqual(student.last_name, 'test_last2')
        self.assertEqual(student.age, 17)

    def test_get_person_endpoint(self):
        response = self.client.get(reverse('person-list'))

        self.assertDictEqual(response.json(),
                             {
                                 'count': 1,
                                 'next': None,
                                 'previous': None,
                                 'results': [{'age': 27,
                                              'email': '',
                                              'first_name': 'test_first',
                                              'last_name': 'test_last',
                                              'person_type': 'STD',
                                              'url': 'http://testserver/api/persons/1/'}]}
                             )

    def test_update_person_endpoint(self):
        student = Person.objects.first()
        self.client.put(reverse(
            'person-detail', kwargs={'pk': student.pk}
        ),
            data={
                'first_name': 'new_test_first',
                'last_name': student.last_name,
                'age': student.age})
        student = Person.objects.first()
        self.assertEqual(student.first_name, 'new_test_first')

    def test_delete_person_endpoint(self):
        student = Person.objects.first()
        self.client.delete(reverse('person-detail', kwargs={'pk': student.pk}))
        self.assertEqual(Person.objects.count(), 0)


class GroupViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user.set_password('test_pass')
        self.user.save()

        self.client.login(username='test_user', password='test_pass')
        self.group = Group.objects.create(name='331a')

    def test_create_group_endpoint(self):
        self.client.post(reverse('group-list'),
                         data={'name': '531a'})
        self.assertEqual(Group.objects.count(), 2)
        group = Group.objects.all()[1]
        self.assertEqual(group.name, '531a')

    def test_get_group_endpoint(self):
        response = self.client.get(reverse('group-list'))

        self.assertDictEqual(response.json(),
                             {
                                 'count': 1,
                                 'next': None,
                                 'previous': None,
                                 'results': [{'url': 'http://testserver/api/groups/1/',
                                              'name': '331a',
                                              'headman': None}]}
                             )

    def test_update_group_endpoint(self):
        group = Group.objects.first()
        self.client.put(reverse(
            'group-detail', kwargs={'pk': group.pk}
        ),
            data={'name': '341a'})
        group = Group.objects.first()
        self.assertEqual(group.name, '341a')

    def test_delete_group_endpoint(self):
        group = Group.objects.first()
        self.client.delete(reverse('group-detail', kwargs={'pk': group.pk}))
        self.assertEqual(Person.objects.count(), 0)


class SubjectViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user.set_password('test_pass')
        self.user.save()

        self.client.login(username='test_user', password='test_pass')
        self.subject = Subject.objects.create(name='Chemistry')

    def test_create_subject_endpoint(self):
        self.client.post(reverse('subject-list'),
                         data={'name': 'Cooking'})
        self.assertEqual(Subject.objects.count(), 2)
        subject = Subject.objects.all()[1]
        self.assertEqual(subject.name, 'Cooking')

    def test_get_subject_endpoint(self):
        response = self.client.get(reverse('subject-list'))

        self.assertDictEqual(response.json(),
                             {
                                 "count": 1,
                                 "next": None,
                                 "previous": None,
                                 "results": [
                                     {
                                         "url": "http://testserver/api/subjects/1/",
                                         "name": "Chemistry"
                                     }]})

    def test_update_subject_endpoint(self):
        subject = Subject.objects.first()
        self.client.put(reverse(
            'subject-detail', kwargs={'pk': subject.pk}
        ),
            data={'name': 'Math'})
        subject = Subject.objects.first()
        self.assertEqual(subject.name, 'Math')

    def test_delete_subject_endpoint(self):
        subject = Subject.objects.first()
        self.client.delete(reverse('group-detail', kwargs={'pk': subject.pk}))
        self.assertEqual(Person.objects.count(), 0)


class CourseViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user.set_password('test_pass')
        self.user.save()

        self.client.login(username='test_user', password='test_pass')
        self.course = Course.objects.create(name='Third')

    def test_create_subject_endpoint(self):
        self.client.post(reverse('course-list'),
                         data={'name': 'Fourth'})
        self.assertEqual(Course.objects.count(), 2)
        course = Course.objects.all()[1]
        self.assertEqual(course.name, 'Fourth')

    def test_get_subject_endpoint(self):
        response = self.client.get(reverse('course-list'))

        self.assertDictEqual(response.json(),
                             {
                                 "count": 1,
                                 "next": None,
                                 "previous": None,
                                 "results": [
                                     {
                                         "url": "http://testserver/api/courses/1/",
                                         "name": "Third"
                                     }
                                 ]
                             })

    def test_update_subject_endpoint(self):
        course = Course.objects.first()
        self.client.put(reverse(
            'course-detail', kwargs={'pk': course.pk}
        ),
            data={'name': 'Fourth'})
        course = Course.objects.first()
        self.assertEqual(course.name, 'Fourth')

    def test_delete_subject_endpoint(self):
        course = Course.objects.first()
        self.client.delete(reverse('course-detail', kwargs={'pk': course.pk}))
        self.assertEqual(Person.objects.count(), 0)


class LessonViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user.set_password('test_pass')
        self.user.save()

        self.client.login(username='test_user', password='test_pass')
        self.lesson = Lesson.objects.create(subject=None, theme='Chicken', date_of_lesson="2022-06-30T18:50:00Z")

    def test_create_lesson_endpoint(self):
        self.client.post(reverse('lesson-list'),
                         data={
                             "theme": "Fish",
                             "date_of_lesson": "2022-07-05T12:30:00Z"})
        self.assertEqual(Lesson.objects.count(), 2)
        lesson = Lesson.objects.all()[1]
        self.assertEqual(lesson.subject, None)
        self.assertEqual(lesson.theme, 'Fish')
        self.assertEqual(lesson.date_of_lesson, datetime(2022, 7, 5, 12, 30, tzinfo=timezone.utc))

    def test_get_lesson_endpoint(self):
        response = self.client.get(reverse('lesson-list'))

        self.assertDictEqual(response.json(),
                             {
                                 "count": 1,
                                 "next": None,
                                 "previous": None,
                                 "results": [
                                     {
                                         "url": "http://testserver/api/lessons/1/",
                                         "subject": None,
                                         "theme": "Chicken",
                                         "date_of_lesson": "2022-06-30T18:50:00Z"
                                     }]})

    def test_update_lesson_endpoint(self):
        lesson = Lesson.objects.first()
        self.client.put(reverse(
            'lesson-detail', kwargs={'pk': lesson.pk}
        ),
            data={'theme': 'Dessert',
                  'date_of_lesson': lesson.date_of_lesson})
        lesson = Lesson.objects.first()
        self.assertEqual(lesson.theme, 'Dessert')

    def test_delete_lesson_endpoint(self):
        lesson = Lesson.objects.first()
        self.client.delete(reverse('lesson-detail', kwargs={'pk': lesson.pk}))
        self.assertEqual(Person.objects.count(), 0)
