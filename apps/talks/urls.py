from django.urls import path
from . import views

urlpatterns = [
    path('', views.TalkListView.as_view(), name='talk_list'),
    path('create/', views.TalkCreateView.as_view(), name='talk_create'),
    path('<int:pk>/', views.TalkDetailView.as_view(), name='talk_detail'),
    path('<int:pk>/delete/', views.TalkDeleteView.as_view(), name='talk_delete'),
    path('status/<int:pk>/', views.talk_status_view, name='talk_status'),
]