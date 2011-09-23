
from django.conf.urls.defaults import *
from django.conf import settings
import website.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myBlog/', include('myBlog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #(r'^admin/(.*)', admin.site.root),
     (r'^$', website.views.index), 
)
