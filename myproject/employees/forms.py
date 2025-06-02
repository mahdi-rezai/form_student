from django import forms
from .models import employee
import re

class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['first_name', 'last_name', 'age', 'tittlejob', 'password']  # فیلد رمز اضافه شد

        widgets = {
            'password': forms.PasswordInput(),  # نمایش رمز به صورت نقطه
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None or age <= 0:
            raise forms.ValidationError("Age must be a positive integer.")
        return age

    def _validate_alpha(self, value, field_name):
        if value is None or not re.fullmatch(r"[a-zA-Z]+", value):
            raise forms.ValidationError(f"{field_name} must contain only letters (A-Z or a-z) without spaces.")
        return value

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return self._validate_alpha(first_name, "First name")

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return self._validate_alpha(last_name, "Last name")

    def clean_tittlejob(self):
        tittlejob = self.cleaned_data.get('tittlejob')
        return self._validate_alpha(tittlejob, "tittlejob")

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is None or len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password
    
class StudentLoginForm(forms.Form):
    first_name = forms.CharField(label='نام', max_length=100)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
