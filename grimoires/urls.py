from django.urls import path
from . import views

app_name = 'grimoires'

urlpatterns = [
    path('', views.GrimoireListView.as_view(),  name='grimoire_list'),
    path('<int:pk>/', views.GrimoireDetailView.as_view(), name='grimoire_detail'),
    path('<int:grimoire_id>/order/', views.create_order, name='create_order'),
    path('complete/', views.order_complete, name='order_complete'),
]
