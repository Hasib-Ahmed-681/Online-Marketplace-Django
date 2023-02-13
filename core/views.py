from django.shortcuts import render, redirect

# Create your views here.
from item.models import Catagory, Item
from . forms import SignUpForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Catagory.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'post':
        form = SignUpForm(request.post)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {
        'form': form
    })
