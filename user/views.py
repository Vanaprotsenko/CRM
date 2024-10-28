import logging
from django.contrib import messages
from django.shortcuts import render, redirect
from user.models import User


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def auth(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=username)
            if password == user.password:
                request.session['user_id'] = user.id
                request.session['role'] = user.role
                logging.info(f'User "{username}" logged in successfully.')

                if user.role == "admin":
                    return redirect('product_list')
                elif user.role == "manager":
                    return redirect('manager_dashboard')
                elif user.role == "user":
                    return redirect('user_dashboard')
            else:
                messages.error(request, "Invalid username or password")
                logging.warning(f'Invalid password attempt for user "{username}".')
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
            logging.warning(f'Login attempt with non-existent user "{username}".')

    return render(request, 'user/auth.html')
