from django.contrib import admin

# Register your models here.

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # 管理ページのレコード一覧に表示するカラムを設定するクラス
    # レコード一覧にIDとusernameを表示
    list_display = ('id','username')
    # 表示するカラムにリンクを設定
    list_display_links = ('id','username')

# 管理サイトにCustomUser,CustomUserAdminを登録する
admin.site.register(CustomUser,CustomUserAdmin)