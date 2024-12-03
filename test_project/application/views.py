from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# from django.db.models import F, Value, CharField
# # F = Field
# from django.db.models.functions import Concat
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # Використовуємо, щоб робити login_requiered з класами


from .models.user import User
from .models.post import Post
from .models.comment import Comment
from .forms import SignUpForm, LogInForm, PostForm, CommentForm, PostUpdateForm

# Для запуску проєкту Django:
# django-admin startproject test_project
# Потім, для запуску аплікації: (Спочатку, треба перейти у шлях проєкту)
# python manage.py startapp application
# Для запуску (Спочатку треба додати назву аплікації у settings.py):
# python manage.py runserver
# Для мігрування моделей db:
# python manage.py migrate
# Для створення адміна:
# python manage.py createsuperuser
# (Інформація у цьому проєкті:
# admin
# admin@email.com
# 123abc)


# def index(request):  # Старий функціональний ендпоінт
#     posts = Post.objects.all().with_user_info()
#     print(posts)
#     return render(request, "index.html", {"posts": posts})


class IndexView(ListView):  # Новий класовий ендпоінт
    # ListView використовуєтсья для сторінок, що схожі на списокю
    template_name = "index.html"  # HTML, що буде темплейтом
    model = Post  # Модель з якої візбметься все
    context_object_name = "posts"  # Ім'я змінної в Jinja

    def get_queryset(self):  # Якщо ми хочемо більш специфічний queryset
        return Post.objects.all().with_user_info()  # Додаємо до querysetу ще інформацію з моделі User


def page1(request):
    return render(request, "page1.html", {})


def page2(request):
    return render(request, "page2.html", {})


def index2(request):
    return HttpResponse("Test")


def page3(request):
    return render(request, "page3.html", {"list": ["item1", "item2", "item3"], "dict": {"key1": "item1", "key2": "item2"}})


# @login_required
# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         print("The request is sent")
#         if form.is_valid():
#             print("form is valid")
#             title = form.cleaned_data["title"]
#             content = form.cleaned_data["content"]
#             user = request.user
#
#             Post.objects.create(title=title, content=content, user=user)
#         return render(request, "create_post.html", {"form": form})
#     form = PostForm()
#     return render(request, "create_post.html", {"form": form})


class PostView(CreateView):
    template_name = "create_post.html"
    form_class = PostForm
    success_url = reverse_lazy("create_post")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                "user": self.request.user,
            }
        )
        return kwargs


# def sign_up(request):  # Старий функціональний ендпоінт
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#         return render(request, "sign_up.html", {"form": form})
#         # username = request.POST["username"]
#         # email = request.POST["email"]
#         # password = request.POST["password"]
#
#         # User.objects.create_user(username=username, email=email, password=password)
#     form = SignUpForm()
#     return render(request, "sign_up.html", {"form": form})


class SignUpView(CreateView):  # Новий класовий ендпоінт
    template_name = "sign_up.html"  # HTML, що буде темплейтом
    # model = User  # Модель в яку будемо додавати рядок
    # fields = ["username", "email", "password"]  # Колонки з якими буде взаємодія. Якщо немає своєї форми, то Django створить форму у змінній form
    form_class = SignUpForm  # Форма, яка буде виокристовуваться. Якщо є це, то можна не писати fields. Також можна не писати model, якщо форма і так вже модел форма
    success_url = reverse_lazy("index")  # URL, у разі успіху

    # def get_success_url(self):  # Схоже на success_url
    #     (pass # Код, щоб отрмати потрібний URL)


def log_in(request):
    if request.method == "POST":
        form = LogInForm(request, request.POST)
        print(form.get_user())
        print(form.errors)
        if form.is_valid():
            print("test")
            login(request, form.get_user())
            return redirect("index")
        return render(request, "log_in.html", {"form": form})
        # username = request.POST["username"]
        # password = request.POST["password"]
        # print(username, password)
    form = LogInForm()
    return render(request, "log_in.html", {"form": form})


class UserLogInView(LoginView):
    template_name = "log_in.html"
    form_class = LogInForm
    redirect_authenticated_user = True


class LogOutView(LogoutView):
    pass


# def create_comment(request):
#     if request.method == "POST":
#         content = request.POST["content"]
#         print(content)
#     form = CommentForm()
#     return render(request, "create_comment.html", {"form": form})


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    http_method_names = ["post"]

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                "user": self.request.user,
                "post": Post.objects.get(id=self.kwargs["id"])
            }
        )
        return kwargs

    def get_success_url(self):  # У разі успіху, відкриється сторінка тогоже поста (перезавантажиться)
        return reverse_lazy("post_detail", kwargs={"id": self.kwargs["id"]})


# def post_detail(request, id):
#     post = Post.objects.get(id=id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             content = form.cleaned_data["content"]
#             user = User.objects.get(id=1)
#
#             Comment.objects.create(content=content, post=post, user=user)
#
#     form = CommentForm()
#
#     return ren+der(request, "post_detail.html", {"post": post, "form": form})


class PostDetailView(LoginRequiredMixin, ModelFormMixin, DetailView):
    model = Post  # Модель, яка потрібна
    pk_url_kwarg = "id"  # Назва атрибуту в URL (по замовчюванню pk)
    template_name = "post_detail.html"  # HTML, який потрібен
    context_object_name = "post"  # Назва об'єкту, шо потрабить у контекст (у Jinja)
    form_class = CommentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                "user": self.request.user,
                "post": self.get_object()
            }
        )
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["post_form"] = PostUpdateForm(initial={"title": post.title, "content": post.content})
        return context
    # def get(self, *args, **kwargs):
    #     post = Post.objects.get(id=self.kwargs["id"])
    #     form = CommentForm
    #     return render(self.request, self.template_name, {"post": post, "form": form})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = CommentForm()
    #     return context


def delete_comment(request, id, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect("index")


@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})


class UpdatePostView(UpdateView):
    form_class = PostUpdateForm
    pk_url_kwarg = "id"
    model = Post
    template_name = "post_detail.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"id": self.kwargs["id"]})


