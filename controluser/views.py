from django.shortcuts import render, redirect
from .models import User
from .forms import userForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

def redirectLogin(request):
    if request.user.is_authenticated:
        return redirect('agendamentos/')
    else:
        return redirect('login/')

# Create your views here.
@login_required()
def listarUser(request):
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})

@login_required()
def createUser(request):
    form = userForm(request.POST or None)
        
    if form.is_valid():
        form.save()
        return redirect('listarUser')

    return render(request, 'cadastrar_usuario.html', {'form': form, 'user': None})

@login_required()
def updateUser(request, id):
    user = User.objects.get(id=id)
    form = userForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('listarUser')

    return render(request, 'cadastrar_usuario.html', {'form': form, 'user': user})

@login_required()
def deleteUser(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('listarUser')

    return render(request, 'delete_prov.html', {'user': user})


@login_required()
def returnLogedUser(request):
    currentUser = request.user


    return render(request, 'profile.html', {'currentuser': currentUser})