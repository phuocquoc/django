from django import  forms

class contrac_form(forms.Form):
    user = forms.CharField(max_length=100)
    email = forms.EmailField()
    body = forms.CharField(widget = forms.Textarea)