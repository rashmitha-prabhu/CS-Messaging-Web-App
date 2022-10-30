from django.shortcuts import render
from .forms import UserForm, ResolveQuery
from django.http import HttpResponseRedirect
from .models import UserQuery

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

def resolve_query(request):
    id = request.get_full_path().strip().split('/')[-2]
    query = UserQuery.objects.get(pk=id)

    if request.method == 'POST':
        form = ResolveQuery(request.POST)
        if form.is_valid():
            query.resolved = True
            query.save()
            return HttpResponseRedirect('/admin/users/userquery')
    else:
        form = ResolveQuery()
    
    return render(request, 'admin/resolve_query.html', {'query': query, 'form': form})

def unresolve_query(request):
    id = request.get_full_path().strip().split('/')[-2]
    query = UserQuery.objects.filter(pk=id).update(resolved=False)
    return HttpResponseRedirect('/admin/users/userquery')