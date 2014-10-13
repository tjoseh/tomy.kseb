from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KSEB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/', 'HelloWorldApp.views.hello',name='hello'),
    url(r'^payroll/$','payroll.views.dashboard',name='dashboard'),
    url(r'^payroll/charts/','payroll.views.charts',name='chart'),
    url(r'^payroll/empfilter/','payroll.views.ajax_emp_filter',name='chart'),
    url(r'^payroll/forms/','payroll.views.forms',name='forms'),
    url(r'^payroll/tables/','payroll.views.tables',name='tables'),
    url(r'^payroll/bootstrap-elements/','payroll.views.bootstrap_elements',name='bootstrap_elements'),
    url(r'^payroll/bootstrap-grid/','payroll.views.bootstrap_grid',name='bootstrap_grid'),
    url(r'^payroll/blank-page/','payroll.views.blank_page',name='blank_page'),
    url(r'^payroll/home/','payroll.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls),))
   
urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_DOC_ROOT + '/static',
        }),
        
)
