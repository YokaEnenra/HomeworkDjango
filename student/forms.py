from django import forms


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=0)
    person_type = forms.CharField(max_length=30)


class SubjectForm(forms.Form):
    subject_name = forms.CharField(max_length=30)
    teacher = forms.IntegerField()
