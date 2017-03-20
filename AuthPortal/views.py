from AuthPortal.forms import UserForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            website = form.cleaned_data['website']
            user.set_password(password)
            user.set_username(username)
            user.set_website(website)
            # add code if you want to login at that moment
        elif form.has_error('email'):
            pass
        elif form.has_error('password'):
            pass
        elif form.has_error('username'):
            pass
    else:
        pass

