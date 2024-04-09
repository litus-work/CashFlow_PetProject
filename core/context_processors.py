from django.db.models import Sum

from .models import Transaction

def total_transaction_amount(request):
    total_amount = Transaction.objects.aggregate(total=Sum('amount'))['total']
    return {'total_transaction_amount': total_amount}
