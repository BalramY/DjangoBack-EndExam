from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserAccountSerializer, UserUpdateSerializer
from django_email_verification import send_email
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from rest_framework import status



class UserLogin(APIView):

	def get(self, request):
		if request.user.is_authenticated:
			return render(request, "home.html")
		else:
			return render(request, "login.html")

	def post(self, request):
		user = authenticate(username=request.data["username"],
					        password=request.data["password"])
		if user:
			login(request, user)
			return Response({"message": "SUCCESS"})
		else:
			user = User.objects.filter(username=request.data["username"])
			if user:
				if user.first().check_password(request.data["password"]) and not user.first().is_active:
					return Response({"message": "NOT_ACTIVE"})
			return Response({"message": "WRONG"})



class Registrations(APIView):
	def get(self, request):
		return render(request, "registration.html")

	def post(self, request):
		if User.objects.filter(username=request.data["username"]):
			return Response({"message": "This email is already used"},
							 status=status.HTTP_406_NOT_ACCEPTABLE)
		request.data._mutable = True
		request.data["email"] = request.data["username"]
		request.data._mutable = False
		serializer = UserAccountSerializer(data=request.data)
		if serializer.is_valid():
			seria_data = serializer.save()
			send_email(seria_data)
			return Response({"message": "SUCCESS"})
		else:
			return	Response({"message": "Something went wrong"},
							  status=status.HTTP_406_NOT_ACCEPTABLE)



class Dashborad(APIView):
	def get(self, request):
		social = SocialAccount.objects.filter(user=request.user)
		if social:
			return render(request, "home.html", {"user": social.first(),
												 "is_not_social_account": False})
		else:
			user = User.objects.get(id=request.user.id)
			return render(request, "home.html", {"user": user,
											     "is_not_social_account": True})


class EditProfile(APIView):
	def get(self, request):
		user = User.objects.get(id=request.user.id)
		return render(request, "edit_profile.html", {"user": user})

	def post(self, request):
		serializer = UserUpdateSerializer(instance=request.user,
										  data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return	Response({"message": "You name is updated."})


class RestPassword(APIView):
	def get(self, request):
		user = User.objects.get(id=request.user.id)
		return render(request, "reset_password.html", {"user": user})

	def post(self, request):
		user = User.objects.filter(id=request.user.id,
							password=request.data["old_password"])
		if user:
			serializer = UserAccountSerializer(instance=request.user,
											   data=request.data, partial=True)
			serializer.is_valid(raise_exception=True)
			serializer.save()
			return Response({"message": "SUCCESS"})
		else:
			return Response({"message": "WENT_WRONG"})


class Logout(APIView):
	def get(self, request):
		django_logout(request)
		return redirect("login")


class ResendEmailVerification(APIView):
	def post(self, request):
		user = User.objects.filter(username=request.data.get("username"))
		if user:
			send_email(user.first())
			return Response({"message": "SUCCESS"})
		else:
			return Response({"message": "WENT_WRONG"},
					 status=status.HTTP_406_NOT_ACCEPTABLE)