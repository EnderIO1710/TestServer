from django.urls import path
from . import views
urlpatterns = [
  #/blog/
	path('', views.blog_home, name='blog-home'),
  #/blog/about/
	path('about/', views.blog_about, name='blog-about'),
]