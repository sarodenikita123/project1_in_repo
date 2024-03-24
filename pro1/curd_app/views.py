from django.shortcuts import render, redirect
from .forms import BankForm
from .models import Bank
from django.http import HttpResponse


def create_view(request):
    template_name = 'curd_app/create.html'
    form = BankForm()
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form field ")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    banks = Bank.objects.all()
    context = {"banks": banks}
    return render(request, template_name, context)


def update_view(request, pk):
    template_name = "curd_app/create.html"
    obj = Bank.objects.get(id=pk)
    form = BankForm(instance=obj)
    if request.method == "POST":
        form = BankForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def cancel_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = Bank.objects.get(id=pk)
    form = BankForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)

