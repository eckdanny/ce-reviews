from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^reviews/', include('customer_reviews.urls', namespace='customer_reviews')),
    url(r'^admin/', include(admin.site.urls)),
)
