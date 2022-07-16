from django.db import models

class Clients(models.Model):
    document = models.CharField(blank=True,max_length=50,null=False, unique=True, verbose_name='Document')
    first_name = models.CharField(blank=True,max_length=100,null=False, verbose_name='First name')
    last_name = models.CharField(blank=True,max_length=100,null=False, verbose_name='Last name')
    email = models.CharField(blank=True,max_length=150,null=False, verbose_name='Email')
    created_on = models.DateField(blank=True,null=False, auto_now_add=True)
    update_at = models.DateField(blank=True,null=False,auto_now_add=True)

    def __str__(self):
        return (self.first_name)


class Products(models.Model):
    name = models.CharField(blank=True,max_length=100, null=False, verbose_name='Name')
    description = models.CharField(blank=True,max_length=250, null=True, verbose_name='Description')
    price = models.FloatField(blank=True,default=0.0, null=False, verbose_name='Price')
    stock = models.IntegerField(blank=True,default=0, null=False, verbose_name='Stock')
    created_on = models.DateField(blank=True,null=False,auto_now_add=True)
    update_at = models.DateField(blank=True,null=False,auto_now_add=True)

    def __str__(self):
        return (self.name)


class Bills(models.Model):
    client_id = models.ForeignKey('Clients',blank=True, on_delete=models.CASCADE,)
    company_name = models.CharField(blank=True,max_length=100, null=False, verbose_name='Company name')
    nit = models.IntegerField(blank=True,null=False, verbose_name='Nit')
    code = models.CharField(blank=True,max_length=255,null=False, unique=True, verbose_name='Code')
    created_on = models.DateField(blank=True,null=False,auto_now_add=True)
    update_at = models.DateField(blank=True,null=False,auto_now_add=True)

    

class BillsProducts(models.Model):
    bill_id = models.ForeignKey('Clients',blank=True,on_delete=models.CASCADE, verbose_name='Bill id')
    product_id = models.ForeignKey('Products',blank=True, on_delete=models.CASCADE , verbose_name='Product id')
    created_on = models.DateField( null=False,auto_now_add=True)
    update_at = models.DateField( null=False,auto_now_add=True)


class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to="static/excel")