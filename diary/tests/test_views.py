from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary

class LoggedInTestCase(TestCase):

    def setUp(self):

        self.password = '<ログインパスワード>'

        self.test_user = get_user_model().objects.create_user(
            username='<ログインユーザー名>',
            email='<ログインユーザーのメールアドレス>',
            password=self.password)

        self.client.login(email=self.test_user.email, password=self.password)

class TestDiaryCreateView(LoggedInTestCase):

    def test_create_diary_success(self):

        params = {'title':'テストタイトル',
                  'content':'本文',
                  'photo1':'',
                  'photo2':'',
                  'photo3':''}

        response = self.client.post(reverse_lazy('diary:diary_create'), params)
        self.assertRedirects(response, reverse_lazy('diary:diary_list'))
        self.assertEqual(Diary.objects.filter(title='テストタイトル').count(),1)

    def test_create_diary_failure(self):
        response = self.client.post(reverse_lazy('diary:diary_create'))
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')

class TestDiaryUpdateView(LoggedInTestCase):

    def test_update_diary_success(self):

        # テスト用日記データの作成
        diary = Diary.objects.create(user=self.test_user, title='タイトル編集前')

        # Postパラメータ
        params = {'title': 'タイトル編集後'}

        # 日記編集処理(Post)を実行
        response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk': diary.pk}), params)

        # 日記詳細ページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('diary:diary_detail', kwargs={'pk': diary.pk}))

        # 日記データが編集されたかを検証
        self.assertEqual(Diary.objects.get(pk=diary.pk).title, 'タイトル編集後')

    def test_update_diary_failure(self):
        """日記編集処理が失敗する事を検証する"""

        # 日記編集処理(Post)を実行
        response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk': 999}))

        # 存在しない日記データを編集しようとしてエラーになる事を検証
        self.assertEqual(response.status_code, 404)


class TestDiaryDeleteView(LoggedInTestCase):
    """DiaryDeleteView用のテストクラス"""

    def test_delete_diary_success(self):
        """日記削除処理が成功する事を検証する"""

        # テスト用日記データの作成
        diary = Diary.objects.create(user=self.test_user, title='タイトル')

        # 日記削除処理(Post)を実行
        response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk': diary.pk}))

        # 日記リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('diary:diary_list'))

        # 日記データが削除されたかを検証
        self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 0)

    def test_delete_diary_failure(self):
        """日記削除処理が失敗する事を検証する"""


        response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk': 999}))


        self.assertEqual(response.status_code, 404)





