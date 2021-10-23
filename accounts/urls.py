from django.urls import path
from .views import (UserLogin,
                    Registrations,
                    Dashborad,
                    EditProfile,
                    RestPassword,
                    Logout,
                    ResendEmailVerification)
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", UserLogin.as_view(), name="login"),
    path("sign-up", Registrations.as_view(), name="sign_up"),
    path("dashboard", login_required(Dashborad.as_view()), name="dashboard"),
    path("edit-profile", login_required(EditProfile.as_view()), name="edit_profile"),
    path("reset-password", login_required(RestPassword.as_view()), name="reset_password"),
    path("logout", login_required(Logout.as_view()), name="logout"),
    path("resend-email-verification", ResendEmailVerification.as_view(),
         name="resend_email_verification")
]


