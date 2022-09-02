from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import upper
from datetime import date
import datetime

from store.forms import *


@login_required(login_url='accounts:login')
def shop(request):
    products = Product.objects.filter(statut='Active')

    data = {
        'products': products
    }
    return render(request, 'store/shop.html', data)


@login_required(login_url='accounts:login')
def product_deal_create(request, slug):
    query = """
                select *
                from store_product
                where store_product.slug=%s
            """

    product = Product.objects.raw(query, [slug])

    if request.method == 'POST':
        form_deal = ObjetDealForm(request.POST, request.FILES)

        d = date.today().strftime("%d%m%Y")
        id_max = ObjetDeal.objects.all().count()

        if (id_max == 0):
            id_max = 1
        else:
            id_max = id_max + 1
        ref = "REQD" + str(d) + '-' + str(id_max)

        if form_deal.is_valid():
            obj = form_deal.save(commit=False)
            obj.nom = upper(obj.nom)
            obj.model = upper(obj.model)
            obj.code = ref
            # print('Nom', obj.nom)
            # print('Model', obj.model)
            # print('Code', obj.code)
            obj.save()
            messages.success(request, "Demande envoyé, le prix et d'autres informations vous seront communiqué dans un délai de 48h.")
            return redirect('store:list_deal')
    else:
        form_deal = ObjetDealForm()
    return render(request, 'store/deal.html', {'form': form_deal, 'product': product})


@login_required(login_url='accounts:login')
def product_desc(request, slug):
    query = """
                    select *
                    from store_product
                    where store_product.slug=%s
                """

    product = Product.objects.raw(query, [slug])

    return render(request, 'store/descript.html', {'product': product})


@login_required(login_url='accounts:login')
def objetdeal_detail(request, imei):
    query = """
                    select *
                    from store_objetdeal
                    where store_objetdeal.imei=%s
                """

    objetdeal = ObjetDeal.objects.raw(query, [imei])

    return render(request, 'store/detail.html', {'objetdeal': objetdeal})


@login_required(login_url='accounts:login')
def update_objetdeal(request, imei):
    obj_desc = get_object_or_404(ObjetDeal, imei=imei)
    form = ObjetDealForm(request.POST or None, instance=obj_desc)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.nom = upper(obj.nom)
        obj.model = upper(obj.model)
        obj.save()
        messages.success(request, "Modification effectuée")
        return redirect('store:list_deal')

    return render(request, 'store/deal_update.html', {'form': form, 'obj_desc': obj_desc})


@login_required(login_url='accounts:login')
def objetdeals_list(request):
    objetdeals = ObjetDeal.objects.filter(customer=request.user, statut='Active').order_by('-id')

    return render(request, 'store/list.html', {'objetdeals': objetdeals})


@login_required(login_url='accounts:login')
def delete_objetdeal(request, imei):
    objetdeal = get_object_or_404(ObjetDeal, imei=imei)

    if request.method == 'POST':
        objetdeal.statut = 'Terminé'
        objetdeal.save()
        messages.success(request, "Suppression effectuée")
        return redirect('store:list_deal')

    return render(request, 'store/deal_delete.html', {'objetdeal': objetdeal})



