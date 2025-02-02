from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('talk_list')

'''
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    '''
def logout_view(request):
    logout(request)
    return redirect('home')  


class RegisterView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Creamos el usuario
        user = form.save()
        if user is not None:
            login(self.request, user)
            return redirect('talk_list')
        return super().form_valid(form)