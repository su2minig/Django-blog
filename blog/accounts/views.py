from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import ProfiledateForm
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from .forms import UserForm

signup = CreateView.as_view(
    form_class = UserForm,
    template_name = 'accounts/form.html',
    success_url = '/accounts/login/'
)

login = LoginView.as_view(
    template_name = 'accounts/login.html',
)

logout = LogoutView.as_view(
    next_page = '/accounts/login/'
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

class ProfileUpdateView(UpdateView):
    model = User 
    form_class = ProfiledateForm 
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/update.html'
