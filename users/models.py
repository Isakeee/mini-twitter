from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        )

    avatar = models.ImageField("Аватарка", upload_to='avatar', null=True, blank=True)



    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
