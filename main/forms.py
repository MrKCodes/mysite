from django import forms



class CreatNewList(forms.Form):
    name = forms.CharField(label="Token", max_length=50)
    check = forms.BooleanField(label="I agree ")