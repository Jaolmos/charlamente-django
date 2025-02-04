from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('talk_list')

def logout_view(request):
    logout(request)
    return redirect('home')  

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('talk_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        return super().form_valid(form)