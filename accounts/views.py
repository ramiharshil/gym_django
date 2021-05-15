from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# #
# # @login_required(login_url="{% url 'user_login' %}")
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            return render(request, 'dashboard.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('user_login')
    else:
        return render(request, 'login.html')



# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['User_name']
#         email = request.POST['Email']
#         password1 = request.POST['password']
#         password2 = request.POST['re-password']
#
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 print("User Taken")
#                 messages.info(request,"username taken")
#                 return render(request, "register.html")
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
#                                            last_name=last_name)
#                 user.save()
#                 print('User Created')
#                 return redirect('user_login')
#     else:
#         return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return redirect('/')


