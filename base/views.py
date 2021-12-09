from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView
from django.views.generic.detail import DetailView
from base.models import tractor,implements
# Create your views here.

def home(request):
    tractors = tractor.objects.all()
    return render(request, 'base/index.html',{'tractors':tractors})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #improve 
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')  
            return redirect('/')
    form=UserCreationForm()
    return render(request, 'base/register.html',{'form':form})

class add_tractor(CreateView):
    model=tractor
    fields=['name','price','implement']
    success_url='/'

    def form_valid(self, form) :
        print('form_valid called')
        object=form.save(commit=False)
        object.owner=self.request.user
        object.save()
        return super(CreateView, self).form_valid(form)

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        raw_password=request.POST['password']
        user=auth.authenticate(username=username, password=raw_password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('user none')
            return redirect('login')
    return render(request, 'base/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


class tractor_list(ListView):
    model=tractor

class tractor_detail(DetailView):
    model=tractor
