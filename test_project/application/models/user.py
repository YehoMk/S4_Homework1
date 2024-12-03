from django.db import models
from django.contrib.auth.models import AbstractUser


__all__ = ("User", )


# В налаштуваннях треба додати AUTH_USER_MODEL = "application.User"
# python manage.py makemigrations (щоб зробити сценарій міграції)
# python manage.py migrate (щоб виконати сценарій)
# Щоб відкатити міграцію:
# python manage.py migrate application <номер міграціїї до якої треба відкатити. Наприклад "0001". "zero", щоб відкатити всі>
# (Якщо додати після цього "--fake", то всі зміни будуть вважатись пропущеними для ORM. Хоча в дб вони залишаться. Це можна використовувати, щоб змінити сценарії)

class User(AbstractUser):
    pass


# python manage.py shell (відкриваємо Django термінал)
#   >>> w (Беремо клас User)
#   >>> User.objects.get(name="Bob") (Беремо користоувача з ім'ям "Bob")
#   >>> users = User.objects.all() (Беремо всіх користувачів)
#   >>> users[0] () (Виводимо першого користувача)
#   >>> users.exists() (Перевіряємо чи існують користувачі)
#   >>> users.count() (Отримужмо кількість користувачів)
#   >>> User.objects.get(id=1) (Беремо користувача з id 1)
#   >>> post = Post(title="Post #1", content="This is a post", user=user_1) (Створюємо екземпляр поста)
#   >>> post.save() (Зберігаємо цей екземпляр у db)
#   >>> print(Post.objects.all().query) (Виписуємо SQL запит для отримання всіх користувачів)
#   >>> Post.objects.create(title="Post #2", content="this is a post", user=user_1) (Відразу створюємо пост в db)

# в Django Post.objects.filter(user__username="Bob") поверне всі пости з юзером в якого ім'я "Bob"
# Для видалення рядку з таблиці
# post = Post(id=1)
# post.delete()
