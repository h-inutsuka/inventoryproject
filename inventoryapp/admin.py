from django.contrib import admin
# modelsからInventoryappクラスをインポート
from .models import Inventoryapp

# Django管理サイトにInventoryappを登録する
admin.site.register(Inventoryapp)