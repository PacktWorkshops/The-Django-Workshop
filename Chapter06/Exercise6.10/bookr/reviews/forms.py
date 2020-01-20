from django import forms

from .models import Publisher


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"
