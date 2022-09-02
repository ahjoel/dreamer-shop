from django.contrib import admin
from django.utils.html import format_html

from store.models import *


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'code', 'libelle', )

    list_display_links = ('id', 'code', 'libelle',)

    search_fields = ('id', 'code', 'libelle',)

    list_filter = ('code', 'code', 'libelle',)


admin.site.register(Categorie, CategorieAdmin)


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if (object.pdt_img):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img))

    thumbnail.short_description = 'Product Image'

    def thumbnail1(self, object):
        if (object.pdt_img_1):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img_1.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img_1))

    thumbnail1.short_description = 'Product Image 1'

    def thumbnail2(self, object):
        if (object.pdt_img_2):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img_2.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img_2))

    thumbnail2.short_description = 'Product Image 2'

    def thumbnail3(self, object):
        if (object.pdt_img_3):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img_3.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.pdt_img_3))

    thumbnail3.short_description = 'Product Image 3'

    list_display = ('id', 'thumbnail', 'thumbnail1', 'thumbnail2', 'thumbnail3', 'code', 'nom', 'model', 'description', 'price', 'statut', 'categorie',)

    list_display_links = ('id', 'thumbnail', 'code', 'nom')

    prepopulated_fields = {"slug": ("nom",)}

    list_editable = ('statut',)

    search_fields = ('id', 'code', 'nom', 'model', 'description', 'price')

    list_filter = ('code', 'nom', 'model', 'description', 'categorie')


admin.site.register(Product, ProductAdmin)


class ObjetDealAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if (object.obj_img):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.obj_img.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.obj_img))

    thumbnail.short_description = 'ObjetDeal Image'

    def thumbnail1(self, object):
        if (object.obj_img_1):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.obj_img_1.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.obj_img_1))

    thumbnail1.short_description = 'ObjetDeal Image 1'

    def thumbnail2(self, object):
        if (object.obj_img_2):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.obj_img_2.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.obj_img_2))

    thumbnail2.short_description = 'ObjetDeal Image 2'

    list_display = ('code', 'imei', 'thumbnail', 'thumbnail1', 'thumbnail2', 'nom', 'model', 'description', 'customer', 'produit', 'price', 'notif', 'statut')

    list_display_links = ('code', 'imei', 'nom',)

    search_fields = ('code', 'imei', 'nom',)

    list_filter = ('code', 'imei', 'nom',)


admin.site.register(ObjetDeal, ObjetDealAdmin)
