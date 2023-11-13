from django.forms import ModelForm
from .models import PhotoPost

# ModelFormを継承したPhotoPostFormクラスを定義
class PhotoPostForm(ModelForm):
    # ModelFormのサブクラス

    class Meta:
        # ModelFormのインナークラス

        # Attributes:
            # model:モデルのクラス
            # fields:フォームで使用するモデルのフィールドを指定
        
        model = PhotoPost
        fields = ['category','title','comment','image1','image2']