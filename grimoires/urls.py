from django.urls import path
from . import views

app_name = 'grimoires'

urlpatterns = [
    path('', views.GrimoireListView.as_view(),  name='grimoire_list'),
    path('<int:pk>/', views.GrimoireDetailView.as_view(), name='grimoire_detail'),
]
