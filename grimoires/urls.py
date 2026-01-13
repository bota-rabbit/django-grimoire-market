from django.urls import path
from . import views
from django.conf import settings    # 開発中用画像関連
from django.conf.urls.static import static    # 開発中用画像関連

app_name = 'grimoires'

urlpatterns = [
    path('', views.GrimoireListView.as_view(),  name='grimoire_list'),
    path('<int:pk>/', views.GrimoireDetailView.as_view(), name='grimoire_detail'),
    path('<int:grimoire_id>/order/', views.create_order, name='create_order'),
    path('complete/', views.order_complete, name='order_complete'),
]

# 開発中用画像関連
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    