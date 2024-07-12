from django import forms
from django.forms.widgets import NumberInput
import datetime


class Student(forms.Form):
    name=forms.CharField(initial ='Your name' )
    name1=forms.CharField(initial ='Your name' )
    comment1=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    comment = forms.CharField(widget=forms.Textarea)
    Email=forms.EmailField(label="please enter your Email")
    check=forms.BooleanField()
    date=forms.DateField()
    date1=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    value=forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    Meal=[('p','pepperoni'),('M','Mahroom'),('B','Beaf')]
    pazza=forms.MultipleChoiceField(choices=Meal,widget=forms.CheckboxSelectMultiple)
    apoinment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    
   
