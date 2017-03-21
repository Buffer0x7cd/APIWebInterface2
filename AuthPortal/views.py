from django.contrib.auth import authenticate, login
from django.shortcuts import render
from CustomUser.models import User
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
from AuthPortal.forms import UserForm,LoginForm


def index(request):
    return render(request,'AuthPortal/portal.html')
def signup(request):
    print("invoke")
    if request.method == 'POST':
        form = UserForm(request.POST)
        users = User.objects.all()
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if users.filter(website=form.cleaned_data['website']).count():
                render(request, 'AuthPortal/portal.html', {
                    'form': form,
                    'error': 'Website already exists',
                    'signup': True,
                })
            if users.filter(phonenumber=form.cleaned_data['phonenumber']).count():
                render(request, 'AuthPortal/portal.html', {
                    'form': form,
                    'error': 'Phone number already exists',
                    'signup': True,
                })
            user.set_password(password)
            user.save()
            return HttpResponse('Hello')
            # add code if you want to login at that moment
        elif form.has_error('email'):
            render(request,'AuthPortal/portal.html',{
                    'form':form,
                'error':'Enter correct Email address',
               'signup': True,
            })
        else:
            return render(request, 'AuthPortal/portal.html',{'signup': True, 'form':form})
    else:
        return render(request,'AuthPortal/portal.html',{'signup': True})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('sucessfull')
            else:
                return render(request, 'AuthPortal/portal.html',
                              {'form': form, 'error_message': 'Your Account is blocked'})
        else:
            return render(request, 'AuthPortal/portal.html',
                          {'form': form, 'error_message': 'Incorrect Credential',})
    return render(request, 'AuthPortal/portal.html')