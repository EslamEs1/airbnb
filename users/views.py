from gc import get_objects
from django.shortcuts import redirect, render
from .forms import SignupForm, UserForm, ProfileForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Profile

class SignupUserForm(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = "Your profile was created successfully"


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'registration/profile.html', {'profile': profile})
    


def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/accounts/profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })