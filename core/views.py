# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from core.forms import TransactionForm
from core.models import Transaction, Category


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile_view(request):
    # Логика для отображения профиля пользователя
    user = request.user  # Получаем текущего пользователя
    return render(request, 'registration/profile.html', {'user': user})
    #return render(request, 'registration/profile.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'  # Указываем имя шаблона
    email_template_name = 'registration/password_reset_email.html'  # Указываем имя шаблона для электронного письма
    success_url = '/password_reset/done/'  # URL-адрес для перенаправления после успешной отправки запроса на сброс пароля

def logout_view(request):
    logout(request)
    return redirect('logout')  # Перенаправление на страницу подтверждения выхода


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transaction_list')  # Укажите здесь имя URL для списка транзакций

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transaction_list')  # Укажите здесь имя URL для списка транзакций

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')  # Укажите здесь имя URL для списка транзакций

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'