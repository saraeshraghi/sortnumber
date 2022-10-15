from django.forms import ModelForm
from django import forms
from .models import Numbers
import random


def random_string():
    return str(random.randint(0, 100))


# class NumbersForm(ModelForm):
    # class Meta:
    #     model = Numbers
    #     fields = '__all__'


class NumbersForm(forms.Form):
    num_1 = forms.CharField(max_length=3, initial=random_string)
    num_2 = forms.CharField(max_length=3, initial=random_string)
    num_3 = forms.CharField(max_length=3, initial=random_string)
    num_4 = forms.CharField(max_length=3, initial=random_string)
    num_5 = forms.CharField(max_length=3, initial=random_string)
    num_6 = forms.CharField(max_length=3, initial=random_string)
    num_7 = forms.CharField(max_length=3, initial=random_string)
    num_8 = forms.CharField(max_length=3, initial=random_string)
    num_9 = forms.CharField(max_length=3, initial=random_string)
    num_10 = forms.CharField(max_length=3, initial=random_string)

    def __init__(self, *args, **kwargs):
        super(NumbersForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

