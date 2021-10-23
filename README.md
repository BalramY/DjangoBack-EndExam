# DjangoBack-EndExam
Django Backend Exam

#TASK DESCRIPTION
I have created apis using DRF where i created these apis login, sign-up, dashboard, edit-profile, reset-password, logout, resend-email-verification and in this project i have used third party libraries which are allauth for google and facebook authentication and django_email_verification to verify the email.

#APIS
1)login:-This is used to login user if the user's email is not verify it will shows the pop to resend email verification code after the successfully verified the user's email user can able to login.

2)sign-up:-This api is used to register the user in which submit is disabled if the user's password is right after that submit button are able to submit the data.

3)dashboard:-It will shows user's email and name if the user's is login from facebook and google and only it have user's email then it will shows user's email and only those user's can see reset password link if they are not login from facebook and google.

4)edit-profile:-It will change user's name.

5)reset-password:-It will change user's password except login from facebook and google.

6)logout:-This api is used to logout the user.

7)resend-email-verification:-This api is used to resend the email if the user haven't verify it's email address.

#THIRD PARTY LIBRARIES
1)allauth:-This library is used to login with facebook and google.
2)django_email_verification:-This library is used to verify user's email address.

#Settings
1):-Sending an email need to define EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in settings.
2):-For testing login with facebook and google need to provide the client id and Secret key of facebook and google in social appilication.

