from django.db import models
# for snippet function
import re, string

# Create your models here.
# extends the Django models.Model class
class Article(models.Model):
    # see documentation for all of the different field types supported
    title= models.CharField(max_length=100)
    # the part of a URL that identifies a page in human-readable keywords is sometimes refered to as the slug (Wikipedia)
    slug= models.SlugField()
    body= models.TextField()
    # auto_now_a=True automatically sets the field to "now" when the object is first created
    date= models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    # add author later

    # string representation
    def __str__(self):
        return self.title

    # function to return a shorter snippet of the larger article
    def snippet(self):
        # help from https://stackoverflow.com/questions/9797357/dividing-a-string-at-various-punctuation-marks-using-split
        # grabing first sentence of a body plus "..."
        return (re.split('[!.?]', self.body)[0] + '...')
