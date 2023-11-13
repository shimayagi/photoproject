from django.urls import path
# Viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views

# URLパターンを逆引きできるようにアプリ名を登録
app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    # http://ホスト名/signup/へのアクセスに対して
    # viewsモジュールのSignupViewをインスタンス化する
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # サインアップ完了ページのビューの呼び出し
    # http://ホスト名/signup_success/へのアクセスに対して
    # viewsモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success/',views.SignUpSuccessView.as_view(), name='signup_success'),

    # ログインページの表示
    # http:///ホスト名/signup へのアクセスに対して
    # django.contrib.auth.views.LoginViewをインスタンス化して
    # ログインページを表示する
    path('login/',
        #  ログイン用のテンプレートフォームをレンダリング
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
        ),

    # ログアウトを実行
    # http:///ホスト名/logout/ へのアクセスに対して
    # django.contrib.auth.views.LogoutViewをインスタンス化して
    # ログアウトさせる
    path('logout/',
        #  ログイン用のテンプレートフォームをレンダリング
        auth_views.LogoutView.as_view(template_name='logout.html'),
        name='logout'
        ),
]
