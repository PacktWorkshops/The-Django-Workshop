from django import forms
from django.core.exceptions import ValidationError

from .models import Publisher, Review


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited", "book"]

    rating = forms.IntegerField(min_value=0, max_value=5)


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("title", "Title"),
                                      ("contributor", "Contributor")
                                  ))

    def clean_search_in(self):
        return self.cleaned_data["search_in"] or "title"


class UploadForm(forms.Form):
    file_upload = forms.FileField()