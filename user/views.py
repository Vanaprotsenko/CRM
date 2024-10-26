from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.models import User


def auth(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('name'), password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'user/user.html')


def users_list(request):
    users = User.objects.all()
    return render(request, 'user/management_users.html', context={'products': users})


@user_passes_test(lambda u: u.role == 'admin')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.name = request.POST.get('name', user.name)
        user.phone = request.POST.get('phone', user.phone)
        new_role = request.POST.get('role', user.role)

        if new_role in dict(User.ROLE_CHOICES).keys():
            user.role = new_role

        user.save()
        messages.success(request, "User details updated successfully.")
        return redirect('user_list')

    context = {
        'user': user,
    }

    return render(request, 'user/edit_user.html', context)
