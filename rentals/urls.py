from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(\d+)/$', views.post_comment, name = 'comment'),
    url(r'^details/(\d+)/$', views.details, name='details'),
    url(r'^about/', views.about, name = 'about'),
    url(r'^filter/', views.filter_price, name='filter_price'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)