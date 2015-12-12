from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='Search')
    min = forms.IntegerField(label='Min')
    max = forms.IntegerField(label='Max')
    lang = forms.CharField(label='Lang')
