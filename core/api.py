from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionListAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionUpdateView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'pk'  # Укажите поле, по которому будет производиться поиск объекта для обновления


class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    lookup_field = 'id'  # Укажите поле, по которому будет производиться поиск объекта для удаления
