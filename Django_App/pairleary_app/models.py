# f,rom email.policy import default
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.utils import timezone



#Userを継承しカラムを追加したクラス


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, verbose_name="ユーザー名", unique=True)
    email = models.EmailField(max_length=100, verbose_name="メールアドレス", unique=True)
    gender_type = models.CharField(max_length=15, default=None, verbose_name="性別", blank=True, null=True)

    def __str__(self):
        return self.username
