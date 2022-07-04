from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('account/', views.account, name='my-account'),
    path('profile/', views.profile, name='profile'),
    path('new_gig/', views.addGig, name='add-gig'),
    path('edit_gig/<int:gigId>/', views.editGig, name='edit-gig'),
    path('gig_detail/<int:gigId>/', views.gigDetail, name='gig-detail'),
]
