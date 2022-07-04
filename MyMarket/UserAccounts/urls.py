from django.urls import path
from . import views

urlpatterns = [
    path('sign_in', views.signIn, name='sign-in'),
    path('sign_out/', views.signOut, name='sign-out'),
    path('sign_up/', views.signUp, name='sign-up'),
]
