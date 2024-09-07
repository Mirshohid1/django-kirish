from django.urls import path
from .views import book_list, alibobo, mening_urgigina_bolama, zumrad_va_qimmat

urlpatterns = [
    path('', book_list, name='book_list'),
    path('alibobo/', alibobo, name='alibobo'),
    path('mening_urgigina_bolama/', mening_urgigina_bolama, name='mening_urgigina_bolama'),
    path('zumrad_va_qimmat/', zumrad_va_qimmat, name='zumrad_va_qimmat'),
]