from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AccountsApp.forms import UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from AccountsApp.models import Avatars

# Create your views here.


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'AccountsApp/profile.html')
            else:
                return render(request, 'AccountsApp/login.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            return render(request, 'AccountsApp/login.html', {'form': form, 'error': 'Invalid username or password'})
    form = AuthenticationForm()
    return render(request, 'AccountsApp/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            form.save()
            return render(request, 'AccountsApp/profile.html', {'user': user, 'message:': 'Account Succesfully created :)'})
    else:
        form = UserRegisterForm()
    return render(request, 'AccountsApp/signup.html', {'form': form})


@login_required
def edit(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #user.username = data['username']
            user.email = data['email']
            user.password1 = data['password1']
            user.password2 = data['password2']
            user.name = data['name']
            user.description = data['description']
            user.web = data['web']
            form.save()
            user = User.objects.get(username=request.user)

            return render(request, 'AccountsApp/profile.html', {'form': form, 'user': user, 'message': 'Account updated successfully'})
    else:
        try:
            form = UserEditForm(initial={ 'email': user.email, 'password1': user.password1,
                                         'password2': user.password2, 'name': user.name, 'description': user.description, 'web': user.web})
        except:
            form = UserEditForm(
                initial={ 'email': user.email})
    return render(request, 'AccountsApp/edit.html', {'form': form})

def profile(request):
    user = request.user
    avatares = Avatars.objects.filter(user=user.id)
    try:
        return render(request, 'AccountsApp/profile.html', {'user': user, 'url':avatares[0].avatar.url})
    except:
        return render(request, 'AccountsApp/profile.html', {'user': user})

def uploadAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            avatar = Avatars(user=user, avatar=form.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'AccountsApp/profile.html', {'user': user, 'message': 'Avatar uploaded successfully'})
    else:
        form = AvatarForm()
    return render(request, 'AccountsApp/uploadAvatar.html', {'form': form})
    