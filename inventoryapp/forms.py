from django.forms import ModelForm
from .models import Inventoryapp

class InventoryappForm(ModelForm):
    class Meta:
        # モデルのクラス
        model = Inventoryapp
        # フォームで使用するモデルのフィールドを指定
        fields = ['category', 'title', 'explanation', 'price', 'inventor', 'image1', 'image2']