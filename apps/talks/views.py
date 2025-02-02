from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Talk
from .forms import TalkForm

class TalkListView(LoginRequiredMixin, ListView):
    model = Talk
    template_name = 'talks/talk_list.html'
    context_object_name = 'talks'

    def get_queryset(self):
        # Filtra las charlas del usuario actual
        return Talk.objects.filter(user=self.request.user)

class TalkCreateView(LoginRequiredMixin, CreateView):
    model = Talk
    form_class = TalkForm  # Cambiamos de fields a form_class
    template_name = 'talks/talk_create.html'
    success_url = reverse_lazy('talk_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TalkDetailView(LoginRequiredMixin, DetailView):
    model = Talk
    template_name = 'talks/talk_detail.html'
    context_object_name = 'talk'

    def get_queryset(self):
        # Asegura que el usuario solo pueda ver sus propias charlas
        return Talk.objects.filter(user=self.request.user)