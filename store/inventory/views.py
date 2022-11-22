from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Stock
from .forms import CreateItem
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.urls import reverse_lazy, reverse


class Things(View):
    def get(self, request):
        return HttpResponse('hello world')


class StoreAdd(View):
    model = Stock
    template = "store/store_add.html"
    success_url = reverse_lazy('inventory:StockList')


    def get(self, request):
        form = CreateItem()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = CreateItem(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        stock = form.save(commit=False)
        # stock.owner = self.request.user
        stock.save()
        return redirect(self.success_url)


class StockView(View):
    model = Stock
    template_name = "store/store_list.html"

    def get(self, request):
        stock_list = Stock.objects.all().order_by('-created_at')
        for st in stock_list:
            st.created_at = naturaltime(st.created_at)

        ctx = {'stock': stock_list}
        return render(request, self.template_name, ctx)


