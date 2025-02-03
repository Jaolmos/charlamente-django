from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Talk
from .forms import TalkForm
from .tasks import process_talk


class TalkListView(LoginRequiredMixin, ListView):
    model = Talk
    template_name = 'talks/talk_list.html'
    context_object_name = 'talks'

    def get_queryset(self):
        # Filtra las charlas del usuario actual
        return Talk.objects.filter(user=self.request.user)

class TalkCreateView(LoginRequiredMixin, CreateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/talk_create.html'
    
    def form_valid(self, form):
        # Guardar el Talk y asignar el usuario
        talk = form.save(commit=False)
        talk.user = self.request.user
        talk.status = 'pending'
        talk.save()
        
        # Lanzar la tarea asíncrona
        process_talk.delay(talk.id)
        
        return redirect('talk_detail', pk=talk.id)

class TalkDetailView(LoginRequiredMixin, DetailView):
    model = Talk
    template_name = 'talks/talk_detail.html'
    context_object_name = 'talk'

    def get_queryset(self):
        # Asegura que el usuario solo pueda ver sus propias charlas
        return Talk.objects.filter(user=self.request.user)