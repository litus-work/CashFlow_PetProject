from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Transaction, Category, Budget, CustomUser, BudgetCategory


class TransactionForm(forms.ModelForm):
    custom_category = forms.CharField(required=False)

    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'description', 'category']
        widgets = {
            'date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        # Создание списка выбора категорий из существующих значений
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        custom_category = cleaned_data.get("custom_category")
        # Проверка, если выбрана категория из списка и введена категория вручную
        if category and custom_category:
            raise forms.ValidationError(
                "Выберите категорию из списка или введите новую, но не оба значения."
            )
        return cleaned_data

    def save(self, commit=True):
        instance = super(TransactionForm, self).save(commit=False)
        custom_category = self.cleaned_data.get('custom_category')
        if custom_category:
            # Создаем новую категорию, если введена пользователем
            category, created = Category.objects.get_or_create(name=custom_category)
            instance.category = category
        if commit:
            instance.save()
        return instance


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['house_rent', 'education', 'transportation', 'food', 'entertainment', 'savings', 'utilities', 'travel', 'communication','sport', 'household', 'healthcare', 'total_budget']



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2')


class BudgetCategoryForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ['name']