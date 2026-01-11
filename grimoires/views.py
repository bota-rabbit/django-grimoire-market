from django.views import generic
from .models import Grimoire

class GrimoireListView(generic.ListView):
    model = Grimoire
    paginate_by = 10    # 1ページに表示する件数
    ordering = ['-created_at']    # 表示順序の指定

class GrimoireDetailView(generic.DetailView):
    model = Grimoire
