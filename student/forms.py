from django import forms


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    age = forms.IntegerField(min_value=0, required=True)
    person_type = forms.CharField(max_length=30, required=True)


class SubjectForm(forms.Form):
    subject_name = forms.CharField(max_length=30, required=True)
    teacher = forms.IntegerField(required=True)


class MessageForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
    to_email = forms.CharField(required=True)
