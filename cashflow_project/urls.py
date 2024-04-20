from django.contrib.auth.views import PasswordResetDoneView, LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from core.api import TransactionListAPIView
from core.views import signup, profile_view, CustomPasswordResetView, logout_view, TransactionListView, \
    TransactionCreateView, TransactionUpdateView, TransactionDeleteView, upload_csv, delete_all_categories, \
    delete_all_transactions, transactions_by_category_view, display_monthly_expense_pie_chart, home, manage_budget, \
    create_budget_category, edit_budget_category, delete_budget_category, budget_category_list, budget_list
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/profile/', profile_view, name='user_profile'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/add/', TransactionCreateView.as_view(), name='transaction_add'),
    path('transactions/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction_edit'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('api/transactions/', TransactionListAPIView.as_view(), name='transaction-list'),
    path('api/transactions/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('api/transactions/update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('api/transactions/delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('transactions/upload-csv/', upload_csv, name='upload_csv'),
    path('transactions/delete_all_transactions-csv/', delete_all_transactions, name='delete_all_transactions'),
    path('transactions/delete_all_categories-csv/', delete_all_categories, name='delete_all_categories'),
    path('transactions/pie_chart/', display_monthly_expense_pie_chart, name='transactions_by_category'),
    path('budget/manage_budget', manage_budget, name='manage_budget'),
    path('budget/create/', create_budget_category, name='create_budget_category'),
    path('budget/category/edit/<int:category_id>/', edit_budget_category, name='edit_budget_category'),
    path('budget/category/delete/<int:category_id>/', delete_budget_category, name='delete_budget_category'),
    path('budget/category/list', budget_category_list, name='budget_category_list'),  # Список категорий бюджета
    path('budget/', budget_list, name='budget_list'),  # Добавленный URL для страницы бюджета
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



