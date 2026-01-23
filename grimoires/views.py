from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Grimoire, Order, OrderItem


class GrimoireListView(generic.ListView):
    model = Grimoire
    paginate_by = 12    # 1ページに表示する件数
    ordering = ['created_at']    # 表示順序の指定

class GrimoireDetailView(generic.DetailView):
    model = Grimoire


@login_required
def create_order(request, grimoire_id):
    grimoire = get_object_or_404(Grimoire, id=grimoire_id)

    # 在庫がなければ購入させない
    if grimoire.stock <= 0:
        return redirect('grimoires:grimoire_detail', pk=grimoire.id)

    # 注文（Order）を作る
    order = Order.objects.create(
        user=request.user,
        status='pending'
    )

    # 注文明細（OrderItem）を作る
    OrderItem.objects.create(
        order=order,
        grimoire=grimoire,
        quantity=1,
        price=grimoire.price
    )

    # 合計金額を保存
    order.total_price = grimoire.price
    order.save()

    # 在庫を減らす
    grimoire.stock -= 1
    grimoire.save()

    return redirect('grimoires:order_complete')

@login_required
def order_complete(request):
    return render(request, 'grimoires/order_complete.html')
