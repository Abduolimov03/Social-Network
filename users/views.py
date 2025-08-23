from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout
from django.views import View
from .forms import MyUserCreationForm, MyuserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User,Follwing
# Create your views here.


class UserLogoutView(View):
    def get(self, request):
        return render(request, "registration/logout")
    

    def post(self, request):
        logout(request)
        return redirect("login")
 



class SignUpView(View):
    def get(self, request):
        form = MyUserCreationForm()
        return render(request, "registration/signup.html", {"form": form})
    
    def post(self, request):
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "registration/signup.html", {"form": form})



class UserUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = MyuserChangeForm(instance=request.user)
        return render(request, "registration/user_update.html", {"form": form})

    def post(self, request):
        form = MyuserChangeForm(instance=request.user, data=request.data, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return(request, "registration/user_update.html", {"form": form})

class ProfileView(LoginRequiredMixin,View):
    def get(self,request,username):
        user=get_object_or_404(User,username=username)
        is_followed=False
        if Follwing.objects.filter(user=user,follower=request.user).exists():
            is_followed=True
        return render(request,'profile.html',{'user':user})



class FollowView(LoginRequiredMixin,View):
    def post(self,request):
        username=request.POST.get('username')
        redirect_url=request.POST.get('redirect_url')
        user = get_object_or_404(User, username=username)

        follwing, created=Follwing.objects.get_or_create(
            user=user,
            follower=request.user
        )
        if not created:
            follwing.delete()
        return redirect(redirect_url)