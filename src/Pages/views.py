from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm

#from .models import User

#from .forms import UserForm

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(request.user)
    #return HttpResponse("<h1>hello world</h1>")
    return render(request, "home.html", {})

def learnPR_view(request, *args, **kwargs):
    return render(request, "learnPR.html", {})

def signIn_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Sign in page</h1>")
    return render(request, "signIn.html", {})

def signOut_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Working Page</h1>")
    return render(request, "signOut.html", {})

def signUp_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Working Page</h1>")
    return render(request, "signUp.html", {})

def user_create_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Working Page</h1>")
    return render(request, "signUp.html", {})

def user_data_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Working Page</h1>")
    return render(request, "signUp.html", {})

def learnPRadv_view(request, *args, **kwargs):
    return render(request, "learnPRadv.html",  {})

def learnLR_view(request, *args, **kwargs):
    return render(request, "learnLR.html", {})

def learnLRadv_view(request, *args, **kwargs):
    return render(request, "learnLRadv.html", {})

def learnLRquiz_view(request, *args, **kwargs):
    return render(request, "learnLRquiz.html", {})

def learnLogR_view(request, *args, **kwargs):
    return render(request, "learnLogR.html",{})

def learnLogRadv_view(request, *args, **kwargs):
    return render(request, "learnLogRadv.html", {})
    

#def signUp_view(request, *args, **kwargs):
#    form = UserForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = UserForm(request.POST or None)
#
#    context = {
#    'form': form
#    }
#    return render(request, "user/signup.html", context)


#def user_create_view(request):
#    form = UserForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = UserForm(request.POST or None)
#
#    context = {
#    'form': form
#    }
#    return render(request, "user/signup.html", context)


def faq_view(request, *args, **kwargs):
    #return HttpResponse("<h1>FAQ Page</h1>")
    return render(request, "faq.html", {})


#def user_data_view(request):
#    obj = User.objects.get(id=1)
#    #context = {
#    #    'firstname': obj.firstname,
#    #    'surname': obj.surname,
#    #    'email': obj.email
#    #}
#    context = {
#    'object': obj
#    }
#    return render(request, "user/data.html", context)

def choosing_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Choosing Page</h1>")
    return render(request, "choosing.html", {})

def quiz_view(request, *args, **kwargs):
    return render(request, "quiz.html", {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('sign in page')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})
