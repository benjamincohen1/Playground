from django.conf.urls import patterns, include, url
from book.views import *
#from book.books import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'book.views.home', name='home'),
    # url(r'^book/', include('book.foo.urls')),
	url(r'^$',root),
	url(r'^time$',time),
	url(r'^num/(\d{1,2})$',dispNum),
	url(r'^hello/$',hello),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^form/$', contact),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
