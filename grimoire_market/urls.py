from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grimoires.urls')),    # トップ：商品一覧
    path('accounts/', include('django.contrib.auth.urls')),    # ログイン系
]
