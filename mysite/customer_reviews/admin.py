from django.contrib import admin
from .models import CustomerReview

# Register your models here.
#admin.site.register(CustomerReview)

class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'isPublished')

admin.site.register(CustomerReview, CustomerReviewAdmin)
