from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    # ЭКСПЕРИМЕНТЫ с формой регистрации
    # def __init__(self, *args, **kwargs):
    #     super(UserCreationForm, self).__init__(*args, **kwargs)
    #     for fieldname in ['username', 'password1', 'password2']:
    #         self.fields[fieldname].help_text = None
    # username = forms.CharField(label='Имя пользователя')
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    email = forms.EmailField(label='Адрес электронной почты', required=True)

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email',)

