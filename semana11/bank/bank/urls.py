from django.conf.urls import patterns, include, url
from django.contrib import admin

#from bank import account
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('account.urls')),
)
