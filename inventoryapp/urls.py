from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BuyItemView

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'Inventoryapp'

# URLパターンを登録するためのリスト
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('looks/', views.LooksView.as_view(), name='Looks'),
    path('all/', views.AllView.as_view(), name='AllItem'),
    path('new/', views.NewView.as_view(), name='NewItem'),
    path('popular/', views.PopularView.as_view(), name='PopularItem'),
    path('Sail/', views.SailView.as_view(), name='SailItem'),
    path('cart/', views.CartView.as_view(), name='Cart'),
    path("create/", views.PageCreateView.as_view(),name="create"),
    path("create/success/", views.FormSuccessView.as_view(),name='formsuccess'),
    path('buy/<int:item_id>/', BuyItemView.as_view(), name='buy_item'),  # ✅ 'buy_item' のURLパターンを定義
    path("confirm/<int:item_id>/", views.DateUp.as_view(), name="confirm"),
    path("buy/success/", views.DateUp.as_view(), name='buysuccess'),

# 詳細ページに関するパス
    path(
        # 詳細ページのURLは「blog-detail/レコードのid」
        'inventory-detail/<int:pk>/',
        # viewsモジュールのInventoryDetailを実行
        views.InventoryDetail.as_view(),
        # URLパターンの名前を'InventoryDetail'にする
        name='inventory_detail'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)