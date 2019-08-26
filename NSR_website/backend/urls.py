from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views
import rest_framework
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.IndexView.as_view(),  name='index'),
    url(r'^test/$', views.TestView.as_view()),
    url(r'^explore/(.+)/$', views.ExploreView.as_view()),
    url(r'^raw_data/(.+)/$', views.RawDataView.as_view()),
    path('explore_post/', views.ExploreView_POST.as_view()),
    url(r'^detail/(.+)/$', views.DetailView.as_view()),
    url(r'^getname/(.+)/$', views.GetNameView.as_view()),
    url(r'^getaddress/$', views.GetAddress.as_view()),
    url(r'^getvibrancyrank/(.+)/$', views.GetVibrancyRankView.as_view()),
]