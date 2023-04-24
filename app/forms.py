from django import forms

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('invalid data')
def check_for_len(value):
    if len(value)<6:
        raise forms.ValidationError('invalid data')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField(max_length=50,validators=[check_for_a])
