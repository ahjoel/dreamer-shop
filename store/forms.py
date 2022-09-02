from django import forms
import datetime
from django.forms import ModelChoiceField
from store.models import *
from accounts.models import *


class ObjetDealForm(forms.ModelForm):
    produit = forms.ModelChoiceField(queryset=Product.objects.filter(statut='Active'), widget=forms.Select(attrs={'class': 'form-control'}))
    imei = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ObjetDeal
        fields = ['produit', 'imei', 'nom', 'model', 'description', 'obj_img', 'obj_img_1', 'obj_img_2', 'customer', 'code', ]


