import email
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from ..models import CustomUser, Orders


#views

class LoginTests(TestCase):
  """loginfuncのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('login'))
    self.assertEqual(response.status_code, 200)

  def setUp(self) -> None:
      """テストメソッド実行前の事前設定"""
      # テスト用アカウントの作成
      self.password = 'password123'
      self.test_user = CustomUser.objects.create_user(
        username='test_user1',
        email='testuser@email.com',
        password=self.password,
        gender_type='男性'
      )
      # テスト用アカウントをログインさせる
      self.client.login(username=self.test_user.username, email=self.test_user.email, password=self.password, gender_type=self.test_user.gender_type)
      self.assertEqual(CustomUser.objects.filter(username='test_user1').count(), 1)


class SignupTests(TestCase):
  """signupfuncのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('signup'))
    self.assertEqual(response.status_code, 200)

  def test_create_user_success(self):
    """ユーザー作成の成功をテスト"""
    # ユーザーデータを作成
    params = {'username': 'test_user2', 'email': 'test2@example.com', 'gender_type': '女性', 'password': 'sjdlkfsl'}
    response = self.client.post(reverse_lazy('signup'), params)
    # ログインページへのリダイレクトを検証
    self.assertRedirects(response, reverse_lazy('login'))
    # データベースへ登録されたことを検証
    self.assertEqual(CustomUser.objects.filter(username='test_user2').count(), 1)


class MatchingTests(TestCase):
  """matchingfuncのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('search_matching'))
    self.assertEqual(response.status_code, 200)


class OrderTests(TestCase):
  """orderfuncのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('create_order'))
    self.assertEqual(response.status_code, 200)


class MypageTests(TestCase):
  """mypagefuncのテストクラス"""

  def setUp(self):
    """
    テスト環境の準備用メソッド。名前は必ず「setUp」とすること。
    同じテストクラス内で共通で使いたいデータがある場合にここで作成する。
    """
    user = CustomUser(id=1, username='test1', email='test1@example.com', gender_type='男性', password = '1234fjdlsaD')

  def test_get_userstatus(self):
    user = CustomUser(id=1, username='test1', email='test1@example.com', gender_type='男性', password = '1234fjdlsaD')
    user.save()

    """
    ユーザーが存在する、変更が反映されているか確認
    """
    url = reverse('mypage')
    create_data = {'username': 'test2', 'email': 'test2@example.com', 'gender_type': '女性', 'password': 'sjdlkfsl'}
    
    response = self.client.post(url, create_data)
    self.assertEqual(response.status_code, 302)
    qs_counter = CustomUser.objects.count()
    self.assertEqual(qs_counter, 1)
    # self.assertEqual(user.username, 'test2')

  def test_get(self):
    """302を返されることを確認"""
    response = self.client.get(reverse('mypage'))
    self.assertEqual(response.status_code, 302)


class TutorialTests(TestCase):
  """tutorialfuncのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('tutorial'))
    self.assertEqual(response.status_code, 200)


# class LogoutTests(TestCase):
#   """logoutfuncのテストクラス"""

#   def test_get(self):
#     """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
#     response = self.client.get(reverse('logout'))
#     self.assertEqual(response.status_code, 200)


# class HeaderTests(TestCase):
#   """headerfuncのテストクラス"""

#   def test_get(self):
#     """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
#     response = self.client.get(reverse('header'))
#     self.assertEqual(response.status_code, 200)
