from django.contrib import admin

from .models import Post, Comment, User


# Додаємо моделі до адмін панелі


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
