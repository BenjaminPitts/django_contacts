from django.urls import path
from . import views

urlpatterns = [
    path('contact_list', views.contact_list, name='contact_list'),
    path('contacts/<int:pk>', views.contact_detail, name='contact_detail'),
    path('contacts/new', views.contact_create, name='contact_create'),
    path('contacts/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete', views.contact_delete, name='contact_delete'),
    path('', views.profile, name='profile'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path("event/click", views.demo_click, name="demo_click"),
    path("error", views.force_error, name="force_error")
]
