from django import forms

class SearchProductFrom(forms.Form):
    Wyszukaj = forms.CharField(max_length=200)