
# f,rom email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
    
#検索条件について定義したテーブル
class Conditions(models.Model):
    condition_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id', null=True)
    category = models.CharField(default='null', max_length=150)
    comment = models.CharField(default='null', max_length=255)

    def __str__(self):
        return self.condition_id

#各種レコードについて定義したテーブル
class Records(models.Model):
    record_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey('Orders', on_delete=models.SET_NULL, to_field='order_id', null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id', null=True)
    condition_id = models.ForeignKey('Conditions', on_delete=models.SET_NULL, to_field='condition_id', null=True)

#予約の日時についてのテーブル
class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    condition_id = models.ForeignKey('Conditions', on_delete=models.SET_NULL, to_field='condition_id', null=True)
    order_date = models.DateTimeField(help_text='予約日付')
    order_time_start = models.DateTimeField(help_text='予約開始時間')
    order_time_end = models.DateTimeField(help_text='予約終了時間')

    def save(self, *args, **kwargs):
        self.order_date = timezone.now()  # 保存されるたびに更新
        return super(Orders, self).save(*args, **kwargs)
