from django import forms
from .models import *
from django.contrib.auth.models import User

class studreg(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),required=True,max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),required=True,max_length=30)
	department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter department'}),required=True,max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),required=True,max_length=30)

	class Meta():
		model = User
		fields = ['username','password']

	def clean_confirm_password(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError("Password Mismatch")
		return confirm_password


# class studform(forms.ModelForm):
# 	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),required=True,max_length=30)

# 	class Meta():
# 		model=studform
# 		fields=['event_code','name']

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )



class UserProctorForm(forms.ModelForm):
    review = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    question = forms.ChoiceField(label='Campus',widget=forms.RadioSelect, choices=(('E', 'Excellent'), ('G', 'Good'), ('A', 'Average'), ('P', 'Poor')))
    question1 = forms.ChoiceField(label='Infra',widget=forms.RadioSelect, choices=(('E1', 'Excellent'), ('G1', 'Good'), ('A1', 'Average'), ('P1', 'Poor')))
    question2 = forms.ChoiceField(label='Canteen',widget=forms.RadioSelect, choices=(('E2', 'Excellent'), ('G2', 'Good'), ('A2', 'Average'), ('P2', 'Poor')))
    question3 = forms.ChoiceField(label='Hello',widget=forms.RadioSelect, choices=(('E3', 'Excellent'), ('G3', 'Good'), ('A3', 'Average'), ('P3', 'Poor')))
    
    
    class Meta:
        model = student
        fields = (
            'review',  
            'question',
            'question1',
            'question2',
            'question3',
            
        )

class EditProctorForm(forms.ModelForm):
    review = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    question = forms.ChoiceField(label='Campus',widget=forms.RadioSelect, choices=(('E', 'Excellent'), ('G', 'Good'), ('A', 'Average'), ('P', 'Poor')))
    question1 = forms.ChoiceField(label='Infra',widget=forms.RadioSelect, choices=(('E1', 'Excellent'), ('G1', 'Good'), ('A1', 'Average'), ('P1', 'Poor')))
    question2 = forms.ChoiceField(label='Canteen',widget=forms.RadioSelect, choices=(('E2', 'Excellent'), ('G2', 'Good'), ('A2', 'Average'), ('P2', 'Poor')))
    question3 = forms.ChoiceField(label='Hello',widget=forms.RadioSelect, choices=(('E3', 'Excellent'), ('G3', 'Good'), ('A3', 'Average'), ('P3', 'Poor')))
    
    
    class Meta:
        model = student
        fields = (
            'review',  
            'question',
            'question1',
            'question2',
            'question3',
            )
        