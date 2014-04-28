from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone
from suppliers.models import Supplier
from .models import CustomerReview

# Create your views here.
def index(request):
    suppliers = Supplier.objects.all().order_by('name')
    context = {'suppliers': suppliers}
    return render(request, 'customer_reviews/index.html', context)

def supplier_reviews(request, supplier_slug):
    supplier = Supplier.objects.get(slug=supplier_slug)
    reviews = CustomerReview.objects.filter(
            supplier__slug=supplier_slug
        ).exclude(
            published__gt=timezone.now()
        ).exclude(
            published__isnull=True
        ).order_by('-published')
    context = {'reviews': reviews, 'supplier': supplier}
    return render(request, 'customer_reviews/reviews.html', context)

def supplier_review_create(request, supplier_slug):
    supplier = Supplier.objects.get(slug=supplier_slug)
    context = {'supplier': supplier}
    if (request.POST):
        # Process data
        try:
            c = CustomerReview(
                supplier=supplier,
                author=request.POST['author'],
                review=request.POST['review'],
            )
            if (request.POST.get('rating')):
                c.rating = request.POST['rating']
            # Validate the model
            c.full_clean()
        except ValidationError as err:
            # No need to make the token obvious
            form_data = request.POST.copy()
            del form_data['csrfmiddlewaretoken']
            return render(request, 'customer_reviews/review-form.html', {
                'supplier': supplier,
                'choices': CustomerReview.RATING_CHOICES,
                'form_data': form_data,
                'errors': err,
            })
        else:
            # Submission was successful
            c.save()
            return HttpResponseRedirect(reverse('customer_reviews:supplier_reviews', args=(supplier_slug,)))
    else:
        # Serve up the form
        context['choices'] = CustomerReview.RATING_CHOICES
        return render(request, 'customer_reviews/review-form.html', context)

def supplier_review_process(request, supplier_slug):
    supplier = get_object_or_404(Supplier, slug=supplier_slug)
    context = {'supplier': supplier, 'choices': CustomerReview.RATING_CHOICES}
    return render(request, 'customer_reviews/review-form.html', context)
