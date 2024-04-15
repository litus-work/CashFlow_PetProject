import csv
import logging
from io import TextIOWrapper

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from core.forms import TransactionForm
from core.models import Transaction, Category
from .forms import CSVUploadForm

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirects to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile_view(request):
    # Logic for displaying a user's profile
    user = request.user  # Get the current user
    return render(request, 'registration/profile.html', {'user': user})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'  # Specify the name of the template
    email_template_name = 'registration/password_reset_email.html'  # Specify the name of the template for the e-mail
    success_url = '/password_reset/done/'  # URL to redirect to after a successful password reset request has been sent


def logout_view(request):
    logout(request)
    return redirect('logout')  # Redirects to the exit confirmation page


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transaction_list')  # Specify here the name of the URL for the transaction list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transaction_list')  # Specify here the name of the URL for the transaction list


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')  # Specify here the name of the URL for the transaction list


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем объект файла из формы
            csv_file = form.cleaned_data['csv_file']

            try:
                # Чтение содержимого CSV-файла в текстовом режиме
                csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'))

                # Пропускаем заголовок, если он есть
                next(csv_data, None)

                # Обработка данных CSV и создание транзакций
                for row in csv_data:
                    # Получение или создание категории
                    category_name = row[3]  # Предполагается, что категория находится в четвертой колонке
                    category, _ = Category.objects.get_or_create(name=category_name)

                    # Создание новой транзакции и сохранение ее в базе данных
                    transaction = Transaction.objects.create(
                        date=row[0],  # Дата предполагается в первом столбце
                        description=row[1],  # Описание предполагается во втором столбце
                        amount=row[2],  # Сумма предполагается в третьем столбце
                        category=category  # Присвоение категории
                    )

                # Успешное завершение обработки CSV и сохранение данных в базе данных
                return render(request, 'transactions/success_upload_csv.html')

            except Exception as e:
                # Ошибка при обработке CSV файла
                return render(request, 'transactions/upload_csv.html', {'form': form, 'error_message': str(e)})

    else:
        form = CSVUploadForm()

    return render(request, 'transactions/upload_csv.html', {'form': form})

def delete_all_transactions(request):
    if request.method == 'POST':
        # Удаление всех транзакций
        Transaction.objects.all().delete()
        return redirect('transaction_list')  # Перенаправление на страницу списка транзакций
    return render(request, 'delete_all_transactions.html')

def delete_all_categories(request):
    if request.method == 'POST':
        # Удаление всех категорий
        Category.objects.all().delete()
        return redirect('transaction_list')  # Перенаправление на страницу списка транзакций
    return render(request, 'delete_all_categories.html')



#
