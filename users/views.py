from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect

# Create your views here.

def get_user_query(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = UserForm()
    return render(request, 'form.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')