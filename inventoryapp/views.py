from django.shortcuts import render, redirect
from .forms import InventoryappForm
from django.urls import reverse_lazy
# django.views.generic.baseからTemplateViewをインポート
# DetailViewは詳細ページに関するパス
from django.views.generic.base import TemplateView
from django.views.generic import ListView,CreateView,UpdateView
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

# モデルBlogPostをインポート
from .models import Inventoryapp

class IndexView(ListView):
    #index.htmlをレンダリングする
    model = Inventoryapp
    template_name = 'index.html'
    context_object_name = 'items'

class InventoryDetail(IndexView):
    '''詳細ページのビュー

    投稿されたものの詳細を表示するのでIndexViewを継承する
    Attributes:
        template_name: レンダリングするテンプレート
        model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name ='index.html'
    # クラス変数modelにモデルInventoryappを設定
    model = Inventoryapp

class LooksView(TemplateView):
    template_name = 'Looks.html'

class AllView(TemplateView):
    template_name = 'All_Items.html'

class NewView(TemplateView):
    template_name = 'New_Items.html'

class PopularView(TemplateView):
    template_name = 'Popular_Items.html'

class SailView(TemplateView):
    template_name = 'Sail_Items.html'

class CartView(TemplateView):
    template_name = 'cart.html'

@method_decorator(login_required, name='dispatch')
class PageCreateView(CreateView):
    form_class = InventoryappForm
    template_name = "page_form.html"

    success_url = reverse_lazy('Inventoryapp:formsuccess')

    def form_valid(self, form):
        postdate = form.save(commit=False)
        postdate.user = self.request.user
        postdate.save()
        return super().form_valid(form)
    
class FormSuccessView(TemplateView):
    template_name = 'page_form_success.html'

class BuyItemView(View):
    template_name = 'buy_success.html'
    """購入処理のビュー"""
    def post(self, request, item_id):
        item = get_object_or_404(Inventoryapp, id=item_id)
        if item.decrease_stock():
            return redirect('Inventoryapp:index')  # 購入後にトップページへリダイレクト
        else:
            return redirect('Inventoryapp:out_of_stock')  # 在庫切れのページへリダイレクト
        
class BuySuccessView(TemplateView):
    template_name = 'buy_success.html'

@method_decorator(login_required, name='dispatch')
class DateUp(UpdateView):
    model = Inventoryapp
    form_class = InventoryappForm
    template_name = "confirm_purchase.html"

    success_url = reverse_lazy('portfolio:index')
    def form_valid(self, form):
        postdate = form.save(commit=False)
        postdate.user = self.request.user
        postdate.save()
        return super().form_valid(form)   