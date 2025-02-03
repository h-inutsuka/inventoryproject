from django.db import models

class Inventoryapp(models.Model):
    CATEGORY = (('pants', 'ズボン'),
                )
    name = models.CharField(max_length=255)  # 商品名
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 価格
    image = models.ImageField(upload_to='products/', default='default.jpg')  # 商品画像
    stock = models.PositiveIntegerField(default=10)# 在庫フィールドを追加

    def __str__(self):
        return self.name

# タイトル用フィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=50,
    )

# 説明文用フィールド
    explanation = models.TextField(
        verbose_name='説明文',
        max_length=300,
    )

# 値段用フィールド(正の整数の10桁のみ許可)
    price = models.PositiveIntegerField(
        verbose_name='値段',
    )

# 在庫用フィールド(正の整数の5桁のみ許可)
    inventor = models.PositiveSmallIntegerField(
        verbose_name='在庫数',
    )

# カテゴリ追加用フィールド
    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=20,
        choices=CATEGORY,
    )

    situation = models.TextField(
        verbose_name='状態'
    )

    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to='photos'
    )

    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to='photos',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title