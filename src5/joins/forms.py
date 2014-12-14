from django import forms

# class EmailForm(forms.Form):
# 	email = forms.EmailField()

from .models import Join
class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ["email",]