from django.contrib.auth.models import AbstractUser, User


class CustomUser(User):
    """拡張ユーザーモデル"""

    class Meta:
        verbose_name_plural = 'CustomUser'
