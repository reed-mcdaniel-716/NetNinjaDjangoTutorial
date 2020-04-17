from django.db import models

# Create your models here.
# extends the Django models.Model class
class Article(models.Model):
    # see documentation for all of the different field types supported
    title= models.CharField(max_length=100)
    # the part of a URL that identifies a page in human-readable keywords is sometimes refered to as the slug (Wikipedia)
    slug= models.SlugField()
    body= models.TextField()
    # automatically adds time that article is created as a field
    date= models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    # add author later

    # string representation
    def __str__(self):
        return self.title
