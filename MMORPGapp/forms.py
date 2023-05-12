from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django import forms
from .models import Post, Comment
from django.contrib.auth.models import Group


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'categories', 'upload')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'upload': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }




class CustomSignupForm(SignupForm):
    subscribe = forms.BooleanField(label='Подписаться на новостную рассылку', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}))


    field_order = ['username', 'email', 'password1', 'password2', 'subscribe']

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        if self.cleaned_data['subscribe']:
            subscribed_group = Group.objects.get(name='subscribed_users')
            subscribed_group.user_set.add(user)

        return user

