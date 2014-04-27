from django.db import models

# TODO: Supplier slugs to be unique or choose another method for this

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name
