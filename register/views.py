from django.shortcuts import render
from .models import UserProfile, UserProfileForm, UserForm, GroupForm,GroupProfile, GroupUserForm
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
        group_user_form = GroupUserForm(request.POST,prefix='user')
        group_profile_form= GroupForm(request.POST,prefix='profile')

        if group_user_form.is_valid()*group_profile_form.is_valid() :
            SaveForm_then_login(request, group_user_form, group_profile_form,'group')
            
            return HttpResponseRedirect(reverse('thanks'))

    else:
        group_user_form = GroupUserForm(prefix='user')
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


class EditProfile(UpdateView):

    success_url= reverse_lazy('home')
    
    def get_object(self, queryset=None):
        if self.request.user.first_name=="group":
            return GroupProfile.objects.get_or_create(user=self.request.user)[0]
        else:
            return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_form_class(self):
        if self.request.user.first_name=="group":
            return GroupForm
        else:
            return UserProfileForm
    def get_template_names(self):
        if self.request.user.first_name=="group":
            return 'edit_profile_group.html'
        else:
            return 'edit_profile_single.html'


def SaveForm_then_login(request,uf,upf,userType):

    user=uf.save(commit=False)
    user.first_name=userType
    
    if userType=='single':
        user.last_name=request.POST['profile-name']
    else : user.last_name=request.POST['user-username']
    
    user.save()
    profile=upf.save(commit=False)
    profile.user=user
    profile.save()

    username=request.POST['user-username']
    password=request.POST['user-password1']
    u=authenticate(username=username,password=password)
    login(request,u)
