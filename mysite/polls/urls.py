from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9+])/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9+])/result$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9+])/vote$', views.vote, name="vote"),
    # url(r'^(?P<case_number>[0-9+])/$', views.)
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]

app_name="polls"
