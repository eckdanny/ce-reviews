from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'customer_reviews/landing.html', context)