from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model
# from ribbonwish.models import User

User = get_user_model()
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(email = email, password = password)
        if not user:
            raise forms.ValidationError("This user does not exist")
        if not user.check_password(password):
            raise  forms.ValidationError("Incorrect password")
        if not user.is_active:
            raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'email2'
            # 'password'
        ]

    def clean(self, *args, **kwargs):
        # first_name = self.cleaned_data('first_name')
        # last_name = self.changed_data('last_name')
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")

        return super(UserRegisterForm,self).clean(*args, **kwargs)

class UserChangeForm(forms.ModelForm):
        """A form for updating users. Includes all the fields on
        the user, but replaces the password field with admin's
        password hash display field.
        """
        password = ReadOnlyPasswordHashField()

        class Meta:
            model = User
            fields = ('email', 'password', 'birth_data', 'is_active', 'is_admin')

        def clean_password(self):
            # Regardless of what the user provides, return the initial value.
            # This is done here, rather than on the field, because the
            # field does not have access to the initial value
            return self.initial["password"]

    # def clean_email2(self):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")
    #     return email
