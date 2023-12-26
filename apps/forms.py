import re 

from django import forms
from django.core.exceptions import ValidationError

# Create your forms here.

class ContactUsForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	phone_number = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	subject = forms.CharField(max_length = 100)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
	
	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')

		# Define the Indian phone number pattern
		# This pattern assumes a 10-digit number starting with 7, 8, or 9
		phone_number_pattern = re.compile(r'^[6789]\d{9}$')

		if not phone_number_pattern.match(str(phone_number)):
			raise ValidationError('Please enter a valid Indian phone number.')

		return phone_number

	def clean_email_address(self):
		email = self.cleaned_data.get('email_address')
		if not email:
			raise ValidationError('Email address is required.')
		return email

	def clean_message(self):
		message = self.cleaned_data.get('message')
		min_length = 10
		max_length = 1000
		if len(message) < min_length or len(message) > max_length:
			raise ValidationError('Message must be between {} and {} characters.'.format(min_length, max_length))
		return message


	def clean_subject(self):
		subject = self.cleaned_data.get('subject')
		if not subject:
			raise ValidationError('Subject cannot be empty.')
		return subject 