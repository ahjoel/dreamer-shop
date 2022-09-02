from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import User


class Categorie(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.libelle}"

    class Meta:
        ordering = ['-created_at', '-id']


class Product(models.Model):
    Active = 'Active'
    Inactive = 'Inactive'
    pdt_choices = [
        (Active, 'Active'),
        (Inactive, 'Inactive'),
    ]

    code = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = RichTextField()
    price = models.IntegerField()

    pdt_img = models.ImageField(upload_to='pdt_img/%Y/%m/%d/')
    pdt_img_1 = models.ImageField(upload_to='pdt_img/%Y/%m/%d/', blank=True)
    pdt_img_2 = models.ImageField(upload_to='pdt_img/%Y/%m/%d/', blank=True)
    pdt_img_3 = models.ImageField(upload_to='pdt_img/%Y/%m/%d/', blank=True)
    slug = models.SlugField(null=False, unique=True)

    statut = models.CharField(choices=pdt_choices, max_length=10, default=Active)

    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return f"{self.nom} - {self.model}"

    class Meta:
        ordering = ['-created_at', '-id']

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str('%s %s' % (self.code, self.nom)))
        return super().save(*args, **kwargs)


class ObjetDeal(models.Model):
    En_cours = 'En cours'
    Terminé = 'Terminé'
    demande_choices = [
        (En_cours, 'En cours'),
        (Terminé, 'Terminé'),
    ]

    code = models.CharField(max_length=200, unique=True)

    imei = models.CharField(unique=True, max_length=30)
    nom = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()

    price = models.IntegerField(null=True, blank=True)
    notif = models.TextField(null=True, blank=True)

    obj_img = models.ImageField(upload_to='obj_img/%Y/%m/%d/')
    obj_img_1 = models.ImageField(upload_to='obj_img/%Y/%m/%d/', blank=True)
    obj_img_2 = models.ImageField(upload_to='obj_img/%Y/%m/%d/', blank=True)

    customer = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    produit = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)

    statut = models.CharField(choices=demande_choices, max_length=10, default=En_cours)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} - {self.model}"

    def __repr__(self):
        return 'Image(%s, %s)' % (self.nom, self.model)

    class Meta:
        ordering = ['-created_at', '-id']




