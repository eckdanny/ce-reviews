from django.shortcuts import render
from suppliers.models import Supplier
from .models import CustomerReview
from django.utils import timezone

# Create your views here.
def index(request):
    suppliers = Supplier.objects.all().order_by('name')
    context = {'suppliers': suppliers}
    return render(request, 'customer_reviews/index.html', context)

def supplier_reviews(request, supplier_slug):
    reviews = CustomerReview.objects.filter(
            supplier__slug=supplier_slug
        ).exclude(
            published__gt=timezone.now()
        ).exclude(
            published__isnull=True
        ).order_by('-published')
    context = {'reviews': reviews}
    return render(request, 'customer_reviews/reviews.html', context)

def supplier_review_create(request, supplier_slug):
    context = {'supplier_slug': supplier_slug}
    return render(request, 'customer_reviews/review-form.html', context)
