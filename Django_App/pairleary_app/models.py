
# f,rom email.policy import default
from django.db import models
from django.contrib.auth.models import User

    
#検索条件について定義したテーブル
class Conditions(models.Model):
    condition_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User", to_field='id', null=True)
    category = models.CharField(default='null', max_length=150)
    comment = models.CharField(default='null', max_length=255)

    def __str__(self):
        return self.condition_id

