from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Talk
from .forms import TalkForm
from .tasks import process_talk

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView



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
        talk = form.save(commit=False)
        talk.user = self.request.user
        talk.status = 'pending'
        talk.save()
               
        process_talk.delay(talk.id)
        
        return redirect('talk_detail', pk=talk.id)

class TalkDetailView(LoginRequiredMixin, DetailView):
    model = Talk
    template_name = 'talks/talk_detail.html'
    context_object_name = 'talk'

    def get_queryset(self):
        # Añadimos un print para debug
        queryset = Talk.objects.filter(user=self.request.user)
        print("Talk queryset:", queryset)  # Para debug
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Context:", context)  # Para debug
        return context
    
class TalkDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Talk
    success_url = reverse_lazy('talk_list')
    success_message = "La charla fue eliminada exitosamente."

    def get_queryset(self):
        return Talk.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        # Obtener y eliminar la charla
        self.object = self.get_object()
        self.object.delete()

        # Si es una petición HTMX, devolver respuesta vacía
        if request.headers.get('HX-Request'):
            return HttpResponse('')
        
        # Si no es HTMX, comportamiento normal (redirección)
        return super().delete(request, *args, **kwargs)
    
    
    
def talk_status_view(request, pk):
    """Vista para actualizar el estado de una charla vía HTMX"""
    talk = get_object_or_404(Talk, pk=pk, user=request.user)
    html = render_to_string('talks/includes/status_badge.html', {'talk': talk})
    
    # Si el estado es final, indicamos a HTMX que detenga las actualizaciones
    headers = {}
    if talk.status in ['completed', 'error']:
        headers['HX-Reswap'] = 'none'
    
    return HttpResponse(html, headers=headers)