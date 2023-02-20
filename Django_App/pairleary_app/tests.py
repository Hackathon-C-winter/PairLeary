import email
from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


def test_is_empty(self):
    """初期状態では何も登録されていないことをチェック"""  
    saved_posts = CustomUser.objects.all()
    self.assertEqual(saved_posts.count(), 0)

class UserTestCase(TestCase):
  def setUp(self):
    """サンプルユーザー作成"""  
    user = CustomUser(username='test', email='test@example.com', gender_type='男性')
    user.save()
    
  def test_saved_single_user(self):
    """サンプルユーザーが登録されているか"""  
    qs_counter = CustomUser.objects.count()
    self.assertEqual(qs_counter, 1)

  # def test_signup(self):
  #     self.assertEqual(self.res.status_code, 302)
  #     assertRedirects(response, expected_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

# 空白の欄を入れてのテスト
# リダイレクト先のテスト
