from django.urls import path
from . import views

urlpatterns = [
    path('', views.TalkListView.as_view(), name='talk_list'),
    path('create/', views.TalkCreateView.as_view(), name='talk_create'),
    path('<int:pk>/status/', views.talk_status_view, name='talk_status'),
    path('<int:pk>/content/', views.talk_content_view, name='talk_content'),
    path('<int:pk>/delete/', views.TalkDeleteView.as_view(), name='talk_delete'),
    path('<int:pk>/', views.TalkDetailView.as_view(), name='talk_detail'),
]