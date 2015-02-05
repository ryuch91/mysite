

import datetime
from django import forms
from polls.models import Survey, Question, Choice

#using for test ---can be deleted---
class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

#using for 'Poll application'
class PhoneNumberField(forms.MultiValueField):
	def __init__(self, *args, **kwargs):
		field=(
			fields.CharField(max_length=3),
			fields.CharField(max_length=4),
			fields.CharField(max_length=4)
		)

class IndividualForm(forms.Form):
	MALE = 'M'
	FEMALE = 'F'
	GENDER = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)
	responder_firstname = forms.CharField(max_length=20, label='First Name', initial='HONG',help_text='Max length is 20.')
	responder_lastname = forms.CharField(max_length=10, label='Last Name', initial='Kil-Dong', help_text='Max length is 10.')
	#responder_phone = forms.PhoneNumberField(label='Your Phone Number',initial='')
	responder_email = forms.EmailField(max_length=30, label='E-mail address', initial='abc@example.com', help_text='Max length is 30.')
	responder_birth = forms.DateField(initial=datetime.date.today, label='Your birthday')
	responder_sex = forms.ChoiceField(choices=GENDER)

class SurveyForm(forms.Form):
	pass
	













