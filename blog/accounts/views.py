from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import AccountUpdateForm
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy

signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = '/accounts/login/'
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

logout = LogoutView.as_view(
    next_page = '/accounts/login/'
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

class AccountUpdateView(UpdateView):
    model = User # 기존 AccountCreateView와 동일한 모델 값을 사용해요.
    form_class = AccountUpdateForm # form을 만들어 값을 전달하게 되요. 
    success_url = reverse_lazy('accountapp:hello_world') # 성공적으로 프로필이 완성되면 메인화면으로 넘겨줍니다.
    template_name = 'accounts/update.html' # template경로 값을 지정해줘요.
    

update = AccountUpdateView.as_view()