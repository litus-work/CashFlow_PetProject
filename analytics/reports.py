from core.models import Transaction
from django.db.models import Sum
import matplotlib.pyplot as plt


def generate_monthly_expense_pie_chart():
    transactions = Transaction.objects.all()
    expenses_by_category = transactions.values('category__name').annotate(total_amount=Sum('amount'))
    labels = [expense['category__name'] for expense in expenses_by_category]
    amounts = [expense['total_amount'] for expense in expenses_by_category]

    # Строим круговую диаграмму
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Monthly Expenses by Category')
    plt.savefig('core/static/reports/pie_report.png')  # Сохранение графика как изображения
    plt.close()  # Закрываем текущее окно графика


def get_transactions_by_category(category_name):
    transactions = Transaction.objects.filter(category__name=category_name)

    return transactions
