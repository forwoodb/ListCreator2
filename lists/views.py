from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeletionMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

# Create your views here.

# Lists

def index(request):
    template = 'index.html'
    if request.user.is_authenticated:
        form = ListNameForm()
        lists = ListName.objects.filter(user=request.user)
        context = {'form': form, 'lists': lists}
        return render(request, template, context)
    else:
        return render(request, template)

@login_required
def add_list(request):
    ln = request.POST['list_name']
    user = request.user
    list_name = ListName(list_name=ln, user=user)
    list_name.save()
    return HttpResponseRedirect('/')


# @login_required
# def delete_list(request, l):
#     x = ListName.objects.get(id=l)
#     x.delete()
#     return HttpResponseRedirect('/')

# Built-in confirm page option
class DeleteListNameView(LoginRequiredMixin, DeleteView):
    model = ListName
    success_url = '/'



# @login_required
# def edit_list(request, l):
#     template = 'edit_list.html'
#     e = ListName.objects.get(id=l)
#     form = UpdateListForm(initial={'list_name': e})
#     context = {'form': form, 'list_name': e}
#     return render(request, template, context)


# @login_required
# def update_list(request, l):
#     up = request.POST['list_name']
#     ln = ListName.objects.get(id=l)
#     ln.list_name = up
#     ln.save()
#     return HttpResponseRedirect('/')

class UpdateListNameView(LoginRequiredMixin, UpdateView):
    model = ListName
    fields = ['list_name']
    success_url = '/'

# Items

@login_required
def list_page(request, l):
    template = 'list_page.html'
    lname = ListName.objects.get(id=l)
    form = ListItemForm()
    li = ListItem.objects.filter(list_n=lname)
    context = {'form': form, 'list_items': li, 'list_name': lname}
    return render(request, template, context)


@login_required
def add_item(request, l):
    lname = ListName.objects.get(id=l)
    item = request.POST['list_item']
    user = request.user
    litem = ListItem(list_n=lname, list_item=item, user=user)
    litem.save()
    return HttpResponseRedirect('/list_page/' + str(l) + '/')


@login_required
def delete_item(request, l, i):
    x = ListItem.objects.get(id=i)
    x.delete()
    return HttpResponseRedirect('/list_page/' + str(l) + '/')

# class DeleteListItemView(DeleteView, DeletionMixin):
#     model = ListItem
#     success_url = reverse_lazy("list_page/list_n/{list_n_id}")


@login_required
def edit_item(request, l, i):
    template = 'edit_item.html'
    e = ListItem.objects.get(id=i)
    ln = ListName.objects.get(id=l)
    form = UpdateItemForm(initial={'list_item': e.list_item})
    context = {'form': form, 'list_item': e, 'list': ln}
    return render(request, template, context)


@login_required
def update_item(request, l, i):
    u = request.POST['list_item']
    list_item = ListItem.objects.get(id=i)
    ln = ListName.objects.get(id=l)
    list_item.list_item = u
    list_item.save()
    return HttpResponseRedirect('/list_page/' + str(ln.id) + '/')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template = 'registration/signup.html'
    success_url = reverse_lazy('index')


def demo_login(request):
    user = authenticate(username='Demo', password='demopassword')
    login(request, user)
    demo_items = ListName.objects.filter(user=user)
    demo_items.delete()
    return redirect('/')
