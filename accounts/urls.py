from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('signup/success/',views.Signup_successView.as_view(),
        name='signup_success'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),
        name='logout'),
    path('logout/success/',auth_views.LogoutView.as_view(template_name='Logout_success.html'),name='logout_success'),
    path('login/',auth_views.LoginView.as_view(template_name='Login.html'),
        name='login'),
    path('login_success/',auth_views.LogoutView.as_view(template_name='Login_success.html'),name='login_success'),
]