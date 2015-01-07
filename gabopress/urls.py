# Django Modules
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^$', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'index', name='index'),
    url(r'^article/(?P<slug>[\w-]+)/$', 'article', name='view_article'),
    url(r'^(?P<year>\d{4})/$', 'list', name="year_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'list', name="month_archive"),
    url(r'^tag/(?P<tag>[\w-]+)/$', 'list', name='tag_archive'),
    url(r'^author/(?P<author>[\w-]+)/$', 'list', name='author_archive'),
    url(r'^confirm/comment/$', 'comment_posted', name='comment_posted'),
    url(r'^post/(?P<slug>[\w-]+)/$', 'view_post', name='view_post'),
)
# Includes static urls settings to main urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Includes media urls settings to main urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
