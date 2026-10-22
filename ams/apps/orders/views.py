from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Если у вас есть модель Order, можете раскомментировать строчку ниже:
# from .models import Order 

def order_list(request):
    return HttpResponse("Список заказов")

def order_create(request):
    return HttpResponse("Создание заказа")

def order_detail(request, pk):
    return HttpResponse(f"Просмотр заказа №{pk}")

def order_complete(request, pk):
    return HttpResponse(f"Заказ №{pk} завершен")

def order_cancel(request, pk):
    return HttpResponse(f"Заказ №{pk} отменен")
