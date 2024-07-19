from django.urls import path 
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm,  MySetPasswordForm



urlpatterns = [
    path('', views.UploadVideo, name='upload-video'),
    path('video-list', views.VideoList, name='video-list'),
    path('sign_up/', views.SignUp, name="sign-up"),
    path("login/", auth_view.LoginView.as_view(template_name="video/login.html", authentication_form=LoginForm), name="login"),
    path("logout/", auth_view.LogoutView.as_view(next_page="login"), name="logout"),

    
    # password reset
    path("password_reset/",auth_view.PasswordResetView.as_view(template_name="video/password_reset.html", form_class=MyPasswordResetForm), name="password_reset"),
        
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name="video/password_reset_done.html"), name='password_reset_done'),
    
    path("password_reset_confirm/<uidb64>/<token>/",auth_view.PasswordResetConfirmView.as_view(template_name="video/password_reset_confirm.html", form_class=MySetPasswordForm), name="password_reset_confirm"),
    
    path("password_reset_complete/",auth_view.PasswordResetCompleteView.as_view(template_name="video/password_reset_complete.html"), name="password_reset_complete"),

]
