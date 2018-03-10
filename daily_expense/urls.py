from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'expense-list/', views.expense_list, name='expense-list'),
    url(r'add-expense/', views.add_expense, name='add-expense'),
    url(r'edit/(?P<expense_id>[0-9]+)/$', views.edit_expense, name='edit-expense'),
    url(r'delete/(?P<expense_id>[0-9]+)/', views.delete_expense, name='delete-expense')
]