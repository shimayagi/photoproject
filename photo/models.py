from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    # 投稿する写真のカテゴリを管理するモデル

    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    
    def __str__(self):
        # オブジェクトを文字列に変換して返す

        # Returns(str):カテゴリ名
        return self.title

class PhotoPost(models.Model):
    # 投稿されたデータを管理するモデル
    # CustomUserモデル（のuser_id)とPhotoPostモデルを
    # 1対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        # ForeigKey =主キー的なもの
        CustomUser,
        verbose_name='ユーザー',
        # ユーザーを削除する場合は、そのユーザーの投稿データも全て削除する
        # on_delete= どこまで削除するか
        on_delete=models.CASCADE
        )

    # Categoryモデル（のtitle)とPhotoPostモデルを
    # 1対多の関係で結びつける
    # Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',    #フィールドのタイトル
        max_length=200             #最大文字200文字
        )
    # コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント',    #フィールドのタイトル
        )
    # イメージのフィールド
    image1 = models.ImageField(
        verbose_name='イメージ１',  #フィールドのタイトル
        upload_to = 'photos'       #MEDIA_PORT以下のphotoにファイルを保存
        )    
    # イメージのフィールド２
    image2 = models.ImageField(
        verbose_name='イメージ２',  #フィールドのタイトル
        upload_to = 'photos',      #MEDIA_PORT以下のphotoにファイルを保存
        blank=True,                #フィールド値の設定は必須ではない
        null=True                   #データベースにnullが保存されることを許容
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',     #フィールドのタイトル
        auto_now_add=True           #日時を自動追加
        )
    
    def __str__(self):
        # オブジェクトを文字列に変換して返す
        # Returns(str)：投稿記事のタイトル
        return self.title