from django.shortcuts import render
from .models import UserProfile, UserProfileForm, UserForm, GroupForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def SingleRegister(request):
    if request.method == "POST":
        
        uf=UserForm(request.POST,prefix='user')
        upf=UserProfileForm(request.POST,prefix='profile')
        if uf.is_valid()*upf.is_valid() :
            
            user=uf.save()
            profile=upf.save(commit=False)
            profile.user=user
            profile.save()

            username=request.POST['user-username']
            password=request.POST['user-password1']
            u=authenticate(username=username,password=password)
            login(request,u)

            return HttpResponseRedirect(reverse('thanks'))
    
    else :
        uf=UserForm(prefix='user')
        upf=UserProfileForm(prefix='profile')

    return render(request,'singleregister.html',{
                                            'userform':uf,
                                            'profileform':upf,
                                    })  


def GroupRegister(request):
    if request.method == 'POST':
        form=GroupForm(request.POST)
        if form.is_valid():

            form.save()

            return HttpResponseRedirect(reverse('thanks'))
    else:
        form=GroupForm()

    return render(request,'groupregister.html',{'form':form,})


@login_required                    
def thanks(request):
    return render(request,'thanks.html')

def home(request):
    return render(request,'home.html')

def help(request):
    return render(request,'helptext.html')