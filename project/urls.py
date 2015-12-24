from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *  
from app.views import *
from django.contrib.auth.views import login, logout
from project import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', login),
    (r'^logout/$', logout),
    (r'^register/$', registerfunction),
    (r'^$', welcomefunction), 
    (r'^main/$', mainfunction),
    (r'^invoicesearch/$', invoicefunction),
    (r'^formsearch/$', formfunction),
    (r'^invoice/$', invoicesearchfunction),
    (r'^form/$', formsearchfunction),
    (r'^edit_invoice/$', invioceupdatefunction),
    (r'^edit_form/$', formupdatefunction),
    (r'^edit_indetail/$', indetailupdatefunction),
    (r'^edit_formdetail/$', formdetailupdatefunction),
    (r'^deleteindetail/$',indetaildeletefunction),
    (r'^deleteformdetail/$',formdetaildeletefunction),
    (r'^add_indetail/$',addindetailfunction),
    (r'^add_formdetail/$',addformdetailfunction),
    (r'^add_invoice/$',addinvoicefunction),
    (r'^add_form/$',addformfunction),
    (r'^zoom_invoice/$',invoicezoomfunction),
    (r'^zoom_form/$',formzoomfunction),
    (r'^print_invoice/$',invoiceprintfunction),
    (r'^print_form/$',formprintfunction),
    (r'^salary/$', salaryfunction),
    (r'^tax/$', taxfunction),
    (r'^taxresult/$', taxresultfunction),
    (r'^salaryresult/$', salary_searchfunction),
    (r'^add/$', addrecordfunction),
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #(r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
