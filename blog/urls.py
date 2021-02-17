from django.urls import path, include
 
from .views import BlogListView, BlogDetailView
from django.views.generic import TemplateView
 
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contacts/', TemplateView.as_view(template_name="contacts.html"), name='contacts'),
    path('', BlogListView.as_view(), name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]