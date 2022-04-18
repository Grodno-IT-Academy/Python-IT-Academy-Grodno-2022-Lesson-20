from django.urls import path
from . import views

app_name = 'auth'
urlpatterns = [
    path('register/', views.register_page, name="reg"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('users/', views.UsersView.as_view(), name='users'),
    path('profile<int:pk>/', views.profile_page, name='profile'),
]