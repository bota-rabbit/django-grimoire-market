from django.db import models
from django.conf import settings

class Grimoire(models.Model):
    title = models.CharField('書名', max_length=200)
    description = models.TextField('解説')
    price = models.PositiveIntegerField('価格')
    stock = models.PositiveIntegerField('在庫数')
    is_active = models.BooleanField('公開中', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', '受付中'),
        ('completed', '完了'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        '状態',
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField('注文日時', auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    grimoire = models.ForeignKey(
        Grimoire,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField('数量')
    price = models.PositiveIntegerField('購入時価格')

    def __str__(self):
        return f'{self.grimoire.title} x {self.quantity}'
