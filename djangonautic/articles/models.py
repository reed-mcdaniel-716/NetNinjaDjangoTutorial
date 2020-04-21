from django.db import models
# for snippet function
import re, string
# importing User model for author
from django.contrib.auth.models import User

# Create your models here.
# extends the Django models.Model class
class Article(models.Model):
    # see documentation for all of the different field types supported
    title = models.CharField(max_length=100)
    # the part of a URL that identifies a page in human-readable keywords is sometimes refered to as the slug (Wikipedia)
    slug = models.SlugField()
    body = models.TextField()
    # auto_now_a=True automatically sets the field to "now" when the object is first created
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # author is link to user who created article
    # if the author it references is deleted, set the author to the default which is None
    author= models.ForeignKey(to= User, on_delete= models.SET_DEFAULT, default= None)

    # string representation
    def __str__(self):
        return self.title

    # function to return a shorter snippet of the larger article
    def snippet(self):
        # help from https://stackoverflow.com/questions/9797357/dividing-a-string-at-various-punctuation-marks-using-split
        # grabing first sentence of a body plus "..."
        return (re.split('[!.?]', self.body)[0] + '...')
