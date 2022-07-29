from rest_framework import serializers

from student.models import Group, Subject, Person, Course, Lesson


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['url', 'first_name', 'last_name', 'email', 'person_type', 'age']


class PersonRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['pk', 'first_name', 'last_name', 'email', 'social_url', 'age', 'person_type', 'student_group']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'headman']


class GroupRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['pk', 'name', 'headman', 'edu_program', 'course', 'subjects']


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['url', 'name']


class SubjectRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['pk', 'name', 'courses']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'name']


class CourseRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['pk', 'name', 'curator']


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['url', 'subject', 'theme', 'date_of_lesson']


class LessonRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['pk', 'subject', 'theme', 'date_of_lesson', 'teacher', 'groups']
