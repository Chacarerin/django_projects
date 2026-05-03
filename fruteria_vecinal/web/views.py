from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from .models import UserProfile

# Vista para la página principal
@login_required
def index(request):
    context = {}
    return render(request, 'index.html', context)

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect(reverse('register'))  
        
        user = User.objects.create_user(
            username=email, 
            email=email, 
            password=password1, 
            first_name=first_name, 
            last_name=last_name
        )

        user = authenticate(username=email, password=password1)
        if user is not None:
            login(request, user)

        messages.success(request, 'Usuario creado exitosamente')
        return redirect('index')
    
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesion Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')