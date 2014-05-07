from django.shortcuts import render
from .models import UserProfile, UserProfileForm, UserForm, GroupForm,GroupProfile
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

MAXGROUPNUMBER = 3


def SingleRegister(request):
    if request.method == "POST":
        
        uf=UserForm(request.POST,prefix='user')
        upf=UserProfileForm(request.POST,prefix='profile')
        if uf.is_valid()*upf.is_valid() :
            
            #use function!

            SaveForm_then_login(request,uf,upf,'single')

            return HttpResponseRedirect(reverse('thanks'))
    
    else :
        uf=UserForm(prefix='user')
        upf=UserProfileForm(prefix='profile')

    return render(request,'singleregister.html',{
                                            'userform':uf,
                                            'profileform':upf,
                                    })  





def GroupRegister(request):
    """
    if len(GroupProfile.objects.all()) >= MAXGROUPNUMBER:
        return render(request,'groupfull.html')
    """
    if request.method == 'POST':
        group_user_form = UserForm(request.POST,prefix='user')
        group_profile_form= GroupForm(request.POST,prefix='profile')

        if group_user_form.is_valid()*group_profile_form.is_valid() :
            SaveForm_then_login(request, group_user_form, group_profile_form,'group')
            
            return HttpResponseRedirect(reverse('thanks'))

    else:
        group_user_form = UserForm(prefix='user')
        group_profile_form = GroupForm(prefix='profile')

    return render(request,'groupregister.html',{
                                            'userform':group_user_form,
                                            'profileform':group_profile_form,
                                        })


@login_required                    
def thanks(request):
    return render(request,'thanks.html')

def home(request):
    return render(request,'home.html')

def help(request):
    return render(request,'helptext.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

"""
class EditProfile(UpdateView):

    def dis(self):
        if self.request.first_name=='single':
            model = UserProfile
            form_class = UserProfileForm
            
        else :
            model = GroupProfile
            form_class = GroupForm
        return model,form_class
        
    model,form_class=dis()

    success_url= reverse_lazy('home')
    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

"""


def EditProfile(request):
    if request.user.first_name=='single':
        class RightView(UpdateView):
            model = UserProfile
            form_class = UserProfileForm
            tempale_name='edit_profile_single.html'
            success_url= reverse_lazy('home')

            def get_object(self, queryset=None):
                return UserProfile.objects.get_or_create(user=self.request.user)[0]
        return RightView
    else :
        
        class RightView(UpdateView):
            model = GroupProfile
            form_class = GroupForm
            tempale_name='edit_profile_group.html'
            success_url= reverse_lazy('home')

            def get_object(self, queryset=None):
                return GroupProfile.objects.get_or_create(user=self.request.user)[0]

    return RightView


def SaveForm_then_login(request,uf,upf,userType):

    user=uf.save(commit=False)
    user.first_name=userType
    user.save()
    profile=upf.save(commit=False)
    profile.user=user
    profile.save()

    username=request.POST['user-username']
    password=request.POST['user-password1']
    u=authenticate(username=username,password=password)
    login(request,u)
