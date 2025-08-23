from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordChangeView, LoginView
from .views import UserLogoutView, SignUpView, UserUpdateView,ProfileView,FollowView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update/", UserUpdateView.as_view(), name="update"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("password-change/", PasswordChangeView.as_view(template_name="registration/pass_change.html"), name="password_change"),
    path("password-change/done", PasswordChangeDoneView.as_view(template_name="registration/pass_change_done.html"), name="password_change_done"),
    path("@<str:username>/",ProfileView.as_view(),name="profile"),
    path('follow/',FollowView.as_view(),name='follow')
]
 