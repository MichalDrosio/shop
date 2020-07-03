from django import forms


class SearchProductFrom(forms.Form):
    query = forms.CharField(max_length=200, label='Szukaj')


