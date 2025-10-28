from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(label="Mot-clé", max_length=100)
