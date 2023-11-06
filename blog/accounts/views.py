from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from accounts.forms import ProfileUpdateForm
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from .forms import UserForm
from django.contrib.auth.mixins import UserPassesTestMixin


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
    form_class = ProfileUpdateForm 
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/update.html'


class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('blog:blog')
    template_name = 'accounts/user_confirm_delete.html'

    def test_func(self):
        return self.get_object() == self.request.user