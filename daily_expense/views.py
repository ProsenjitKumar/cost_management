from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import redirect

# Create your views here.

def expense_list(request):
    all_list = Expense.objects.all()
    return render(request, 'daily_expense/expense_list.html', {'all_expense_list': all_list})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect(to='expense-list')
    else:
        form = ExpenseForm
    return render(request, 'daily_expense/add_expense.html', {'form': form})

def edit_expense(request, expense_id):
    expenses = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expenses)
        form.save()
        return redirect(to='expense-list')
    else:
        form = ExpenseForm(instance=expenses)

    context = {'form': form}
    return render(request, 'daily_expense/edit_expense.html', context)

def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect(to='expense-list')
