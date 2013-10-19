from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
 


urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^services/', TemplateView.as_view(template_name="services.html")),
    url(r'^projects/', TemplateView.as_view(template_name="projects.html")),
    url(r'^about/', TemplateView.as_view(template_name="about.html")), 
    url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)  



if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
