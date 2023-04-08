from django import forms






class InputForms(forms.ModelForm):
    input = forms.TextInput(max_length=100)