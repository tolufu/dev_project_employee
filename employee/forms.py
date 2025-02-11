from django import forms
from .models import Employee,EmployeeTraining,EmployeeSkill,TrainingMaster,SkillMaster
from django.forms import ModelForm



class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employee_id", "last_name", "first_name", "birth_date"]
        widgets = {
            'birth_date':forms.DateInput(attrs={'class': 'form-control', "type":"date"})
        }

class TrainingCreateForm(forms.ModelForm):
    training = forms.ModelChoiceField(
        queryset=TrainingMaster.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    get_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', "type": "date"}),
        required=True
    )

    class Meta:
        model = EmployeeTraining
        fields = ["training", "get_date"]

class SkillCreateForm(forms.ModelForm):
    skill = forms.ModelChoiceField(
        queryset=SkillMaster.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    get_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', "type": "date"}),
        required=True
    )

    class Meta:
        model = EmployeeSkill
        fields = ["skill", "get_date"]
