from django.contrib.auth.forms import UserCreationForm
from .models import User

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'password1', 'password2',]