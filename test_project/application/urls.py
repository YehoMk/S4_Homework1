from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
# Можна додавати на функції

from . import views

urlpatterns = [
    # path("", views.index, name="index"),  # Посилання на старий функціональний ендпоінт
    path("", views.IndexView.as_view(), name="index"),  # Посилання на новий класовий ендпоінт
    path("page1/", views.page1),
    path("page2/", views.page2),
    path("index2/", views.index2),
    path("page3/", views.page3),
    # path("create_post/", views.create_post),
    path("create_post/", views.PostView.as_view(), name="create_post"),
    # path("sign_up/", views.sign_up),  # Посилання на старий функціональний ендпоінт
    path("sign_up/", views.SignUpView.as_view()),  # Посилання на новий класовий ендпоінт
    # path("log_in/", views.log_in),
    path("log_in/", views.UserLogInView.as_view()),
    # path("create_comment/", views.create_comment),
    # path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("post/<int:id>/comment/add", views.CreateCommentView.as_view(), name="create_comment"),
    path("post/<int:id>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:id>/comment/delete/<int:comment_id>", views.delete_comment, name="delete_comment"),
    path("profile/", views.profile),
    path("log_out/", views.LogoutView.as_view(), name="log_out"),
    path("post/<int:id>/update", views.UpdatePostView.as_view(), name="update_view"),
    path("subscribtion_information/", views.SubscriptionInformationView.as_view()),
    path("filter_test/", views.FilterTest.as_view())
]
