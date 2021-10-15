from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from django.views.decorators.http import require_POST, require_safe
from .models import Contact, Phone, Phonetype


@require_safe
def contact_list_page(request):
    page = request.GET.get('page', 1)
    content = Contact.objects.all()
    paginator = Paginator(content, 2)
    try:
        content = paginator.page(page)
    except EmptyPage:
        content = paginator.page(1)
    return render(request, 'list.html', {'contacts': content})




def home(request):
    return render(request, 'index.html', {})


@require_safe
def details(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'details.html', {'contact': contact})


@require_safe
def create_page(request):
    choises = Phonetype.proccess()
    return render(request, "create.html", {'choises': choises})


@require_POST
def create(request):
    name = request.POST['name']
    number = request.POST['number']
    _type = request.POST['type']
    contact = Contact(name=name)
    contact.save()
    phone = Phone(number=number, type=_type, contacts=contact)
    phone.save()
    messages.info(request, 'Successfully created', extra_tags='success')
    return redirect('contact:contact')


def delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('contact:contact')


def delete_page(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'delete.html', {'contact': contact})


def add_page(request, pk):
    choise = Phonetype.proccess()
    contact = Contact.objects.get(pk=pk)
    return render(request, 'add_page.html', {'choises': choise, 'contact': contact})


def add(request, pk):
    contact = Contact.objects.get(pk=pk)
    number = request.POST['number']
    _type = request.POST['type']
    phone = Phone(number=number, type=_type, contacts=contact)
    phone.save()
    return redirect('contact:detail', pk=pk)
