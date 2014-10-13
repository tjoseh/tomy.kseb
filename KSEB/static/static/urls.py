from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KSEB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/', 'HelloWorldApp.views.hello',name='hello'),
    url(r'^payroll/','payroll.views.home',name='home'),
    url(r'^kseb/', include(admin.site.urls)),
    
)
urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_DOC_ROOT + '/static/'
        }),
        
        
)
