from django import forms


class StudentRegister(forms.Form):
    name = forms.CharField(
        initial='Hassan', label='Your Name',
        label_suffix="  -->  ", help_text='Name must be 15 char',)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'class1'}), label_suffix="  -->  ")
    email = forms.CharField(
        widget=forms.EmailInput, label_suffix="  -->  ")
