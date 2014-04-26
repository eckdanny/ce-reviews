from django.db import models
from django.utils import timezone

# Create your models here.
class CustomerReview(models.Model):
    # Factor Data (implementation just happens to be numeric)
    # ENUM for greater flexibility
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    supplier = models.ForeignKey('suppliers.Supplier')
    author = models.CharField(max_length=60)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    published = models.DateTimeField(editable=True, blank=True, null=True)

    def __unicode__(self):
        return self.review

    def isPublished(self):
        if (self.published and self.published <= timezone.now()):
            return True
        else:
            return False
    isPublished.admin_order_field = 'published'
    isPublished.boolean = True
    isPublished.short_description = 'Is Published?'
