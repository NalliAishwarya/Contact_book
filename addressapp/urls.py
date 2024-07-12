from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home/contact/', views.contact, name='contact'),
    path('home/register/', views.register, name='register'),
    path('home/sign_in/', views.sign_in, name='sign_in'),
    path('home/profile/<int:user_id>/', views.profile, name='profile'),
    path('home/useradd/<int:user_id>/', views.useradd, name='useradd'),
    path('home/update/<int:user_id>/<int:contact_id>/', views.update, name='update'),
    path('home/delete/<int:user_id>/<int:contact_id>/', views.delete, name='delete'),
    path('home/search-area/<int:id1>',views.profile1,name="search-area"),
    path('home/sort_contacts/<int:id2>', views.sort_contacts, name='sort_contacts'),
]