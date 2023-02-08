# f,rom email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#Userを継承しカラムを追加したクラス
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, verbose_name="ユーザー名", unique=True)
    gender_type = models.CharField(max_length=1, choices=[(None, "--"), ("m", "男性"), ("f", "女性")], default=None, verbose_name="性別", blank=True, null=True)

    def __str__(self):
        return self.username
    
#検索条件について定義したテーブル
# class Conditions(models.Model):
#     condition_id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id', null=True)
#     category = models.CharField(default='null', max_length=150)
#     comment = models.CharField(default='null', max_length=255)

#     def __str__(self):
#         return self.condition_id

#各種レコードについて定義したテーブル
# class Records(models.Model):
#     record_id = models.IntegerField(primary_key=True)
#     order_id = models.ForeignKey('Orders', on_delete=models.SET_NULL, to_field='order_id', null=True)
#     user_id = models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id', null=True)
#     condition_id = models.ForeignKey('Conditions', on_delete=models.SET_NULL, to_field='condition_id', null=True)

#予約テーブル
class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id', null=True,related_name='user_id')
    order_date = models.DateTimeField(help_text='予約日付')
    order_time_range_type = models.CharField(default='null',max_length=10)
    category = models.CharField(default='null', max_length=150)
    hope_gender_type = models.CharField(max_length=1, choices=[(None, "--"), ("m", "男性"), ("f", "女性")], default=None, verbose_name="性別", blank=True, null=True)
    comment = models.CharField(default='null', max_length=255)
    matched_user_id = models.IntegerField(primary_key=False, default='null',null=True)

    def save(self, *args, **kwargs):
        self.order_date = timezone.now()  # 保存されるたびに更新
        return super(Orders, self).save(*args, **kwargs)