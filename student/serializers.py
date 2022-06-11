from rest_framework import serializers

from student.models import Group, Subject, Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['url', 'first_name', 'last_name', 'email', 'person_type']


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
