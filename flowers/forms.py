from django import forms

class MyFilterForm(forms.Form):
    FILTER_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    filter_option = forms.ChoiceField(choices=FILTER_CHOICES, required=False)