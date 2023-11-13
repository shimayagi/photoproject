from django.db import models

from django.contrib.auth.models import AbstractUser

# AbstractUserを継承したCustomUserを定義
class CustomUser(AbstractUser):

    # Userモデルを継承したカスタムユーザーモデル
    pass
