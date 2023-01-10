from django import forms
from .models import Appointments

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields =[
        'title',
        'date',
        'time',
        'phone_number',
        'customer_name',
        'email',
        ]
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }