from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page_url'),
    path('about/', about, name='about_url'),
    path('contacts/', contacts, name='contacts_url'),
    path('projects/', projects, name='projects_url'),
    path('reviews/', reviews, name='reviews_url'),
    path('get_contact/',get_contact, name='get_contact_url'),
    path('get_review/', get_reviews, name='get_review_url'),
    path('project_detail/<pk>', project_detail, name='project_detail_url')
]