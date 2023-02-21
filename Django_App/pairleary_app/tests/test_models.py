import email
from unicodedata import category
from django.test import TestCase
from django.urls import reverse
from ..models import CustomUser, Orders


# docker compose -f docker-compose.yml exec app python manage.py test
# によりテストします


#ブランク状態確認
def test_is_empty_user(self):
    """初期状態では何も登録されていないことをチェック(CustomUser)"""  
    saved_posts = CustomUser.objects.all()
    self.assertEqual(saved_posts.count(), 0)

def test_is_empty_orders(self):
    """初期状態では何も登録されていないことをチェック(Orders)"""  
    saved_posts = Orders.objects.all()
    self.assertEqual(saved_posts.count(), 0)

#CustomUserのテスト
class UserTestCase(TestCase):
  def setUp(self):
    """サンプルユーザー作成"""  
    user = CustomUser(username='test', email='test@example.com', gender_type='男性')
    user.save()
    
  def test_saved_single_user(self):
    """サンプルユーザーが登録されているか"""  
    qs_counter = CustomUser.objects.count()
    self.assertEqual(qs_counter, 1)

  #上2つをコメントアウトしてから実行
  # def test_saving_and_retrieving_user(self):
  #   """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
  #   user = CustomUser()
  #   username = 'test_username'
  #   password = 'test_password_to_retrieve123'
  #   email = 'aaa@example.com'
  #   gender_type = '男性'

  #   user.username = username
  #   user.password = password
  #   user.email = email
  #   user.gender_type = gender_type
  #   user.save()

  #   saved_users = CustomUser.objects.all()
  #   actual_user = saved_users[0]

  #   self.assertEqual(actual_user.username, username)
  #   self.assertEqual(actual_user.password, password)
  #   self.assertEqual(actual_user.email, email)
  #   self.assertEqual(actual_user.gender_type, gender_type)


#Ordersのテスト
class OrdersTestCase(TestCase):
  def setUp(self):
    """サンプルユーザー作成"""  
    user_1 = CustomUser(id=1, username='test1', email='test1@example.com', gender_type='男性')
    user_1.save()

    user_2 = CustomUser(id=2, username='test2', email='test2@example.com', gender_type='男性')
    user_2.save()

    user_3 = CustomUser(id=3, username='test3', email='test3@example.com', gender_type='男性')
    user_3.save()

    """新規予約作成"""  
    order = Orders(order_date='2023-02-24', order_time_range_type='午前', category='開発', hope_gender_type='男性', comment='aaaa', matched_user_id_id=None, user_id_id=None)
    order.save()

    #投稿とuserのidが紐付いている予約
    order_user = Orders(order_date='2023-02-24', order_time_range_type='午前', category='開発', hope_gender_type='男性', comment='aaaa', matched_user_id_id=None, user_id_id=2) 
    order_user.save()

    #投稿とuserのidが紐付いている&マッチングが成立した予約
    matched_user = Orders(order_date='2023-02-24', order_time_range_type='午前', category='開発', hope_gender_type='男性', comment='aaaa', matched_user_id_id=3, user_id_id=1)
    matched_user.save()
  
  def test_saved_order(self):
    """新規予約が登録されているか"""  
    qs_counter = CustomUser.objects.count()
    self.assertEqual(qs_counter, 3)
    
