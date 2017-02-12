# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#Add: auth views;
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
]

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^filer/', include('filer.urls')),
    url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),
    url(r'^djangocms_comments/', include('djangocms_comments.urls')),

    #django allauth
    #url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    #url(r'^accounts/', include('registration.backends.simple.urls')),

    #add: direct link to login and out;
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    #spirit:
    #url(r'^forum/', include('_cms.apps.forum.urls'), app_name='forum'),

    #people:
    #url(r'^authors/', include('ssrd_people.urls'), app_name='ssrd_people'),

    #search:
    #url(r'^search/', include('aldryn_search.urls')),

    # keep this in the last line
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
