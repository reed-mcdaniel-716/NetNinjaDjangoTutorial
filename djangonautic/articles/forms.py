# import forms module
from django import forms
# import our own models
from . import models

# class for article creation which extends the ModelForm class
class CreateArticle(forms.ModelForm):
    class Meta:
        # what Model are we working from?
        model= models.Article
        # what fields of this Model do we want?
        # date is automatic
        fields= ['title', 'slug', 'body', 'thumb']
