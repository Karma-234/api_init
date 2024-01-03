from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import *


def recipe(request: HttpRequest):

    if request.method == "POST":
        data = request.POST
        textFils = request.FILES
        name = data.get('recipeName')
        descriprion = data.get('description')
        files = textFils.getlist('inputFile')
        cookingDate = data.get('cookingDate')
        print(data)
        UserRecipe.objects.create(
            name=name, description=descriprion, cookingDate=cookingDate, images=files[0])
        return redirect('/recipe/')
    querySet = UserRecipe.objects.all()
    context = {'recipes': querySet}
    if request.GET.get('search'):
        print(request.GET.get('search'))
        querySet = querySet.filter(name__icontains=request.GET.get('search'))
        context = {'recipes': querySet}

    return render(request=request, template_name='recipe/index.html', context=context)


def delete_recipe(request: HttpRequest, id):
    querySet = UserRecipe.objects.get(id=id)
    querySet.delete()
    print(request.method)
    return redirect("/recipe/")


def update_recipe(request: HttpRequest, id):
    querySet = UserRecipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        textFils = request.FILES
        name = data.get('recipeName')
        descriprion = data.get('description')
        files = textFils.getlist('inputFile')
        print(request.method)
        print(querySet.description)
        querySet.name = name
        querySet.images = files[0] if len(files) > 0 else files[0]
        querySet.description = descriprion
        querySet.save()
        return redirect('/recipe/')

    context = {'id': id, 'name': querySet.name,
               'description': querySet.description, 'image': querySet.images}
    return render(request=request, template_name='recipe/update.html', context=context)


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        userName = data.get('userName')
        password = data.get('password')
        user = User.objects.filter(username=userName)
        if user.exists():
            authUser = authenticate(
                request=request, username=userName, password=password)
            if authUser is None:
                messages.info(request=request,
                              message='Invalid login details!')
                return redirect('/login/')
            else:
                user.update(is_active=True)
                test = login(request=request, user=authUser)
                print(authUser.get_session_auth_hash)
                return redirect('/recipe/')

        else:
            messages.info(request=request, message='Invalid login details!')
            return redirect('/login/')

    return render(request=request, template_name='recipe/login.html')


def register(request):
    if request.method == 'POST':
        data = request.POST
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        userName = data.get('userName')
        password = data.get('password')
        user = User.objects.filter(username=userName)
        if user.exists():
            messages.info(request=request, message='User already registered!')
            return redirect('/register/')
        user = User.objects.create(first_name=firstName,
                                   last_name=lastName, username=userName)
        user.set_password(password)
        user.save()
        messages.info(request=request, message='Account created successfully!')
    return render(request=request, template_name='recipe/register.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')
