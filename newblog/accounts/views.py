from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1']
            )
            return redirect('home')
        else :
            return render(request, 'accounts/signup.html')  #비밀번호 다릅니다 해주던가 해도 댐 새로 html 만들어서
    else:
        return render(request, 'accounts/signup.html')