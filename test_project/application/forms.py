from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Post, Comment, User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LogInForm(AuthenticationForm):
    pass


# Форм створена з Django
# class SignUpForm(forms.Form):
#     username = forms.CharField(label="Username", min_length=3, max_length=30, widget=forms.TextInput(attrs={"required": True, "placeholder": "username"}))
#     email = forms.CharField(label="Email", min_length=3, max_length=30, widget=forms.EmailInput(attrs={"required": True, "placeholder": "example@email.com"}))
#     password = forms.CharField(label="Password", min_length=3, max_length=30, widget=forms.PasswordInput(attrs={"required": True, "placeholder": "password"}))


# class LogInForm(forms.Form):
#     username = forms.CharField(label="Username", min_length=3, max_length=30, widget=forms.EmailInput(attrs={"required": True, "placeholder": "example@email.com"}))
#     password = forms.CharField(label="Password", min_length=3, max_length=30, widget=forms.PasswordInput(attrs={"required": True, "placeholder": "password"}))


# class CreatePostForm(forms.Form):
#     title = forms.CharField(label="Title", min_length=3, max_length=30, widget=forms.TextInput(attrs={"required": True, "placeholder": "title"}))
#     content = forms.CharField(label="Content", min_length=3, max_length=120, widget=forms.Textarea(attrs={"required": True, "placeholder": "content"}))


class PostAbstractForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

        def clean_title(self):  # Валідація
            title = self.cleaned_data.get("title")
            if len(title) > 20:
                raise ValidationError("Title must be less than 20 characters long")
            return title


# Форм створена з Django на основі моделі в дб
class PostForm(PostAbstractForm):
    # def clean(self):
    #     title = self.cleaned_data.get("title")
    #     if len(title) > 100:
    #         pass

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.instance.user = user


class PostUpdateForm(PostAbstractForm):
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        post = kwargs.pop("post")
        super().__init__(*args, **kwargs)
        self.instance.user = user
        self.instance.post = post
