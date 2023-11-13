from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # UserCreationFormのサブクラス
    class Meta:
        # UserCreationFormのインナークラス
        # Attributes:
            # model連携するUserモデル
            # fields:フォームで使用するフィールド
            # 連携するUserモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、パスワード
        fields = ('username','email','password1','password2')

