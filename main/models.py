from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse


class Supplier(models.Model):
    
   name = models.CharField('Поставщик', max_length=100)
   address = models.CharField('Адрес', max_length=100)
   tel = models.CharField('Телефон', max_length=10)
   
   def __str__(self):
       return self.name
     
   class Meta:
      verbose_name = 'Поставщик'
      verbose_name_plural = 'Поставщики'
      
      
   
class Products(models.Model):
    
   
   title = models.CharField('Название Продукта', max_length=100, unique=True)
   description = models.TextField('Описание Продукта')
   price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
   amount = models.IntegerField('Склад', default=0)
   supplier = models.ForeignKey(Supplier, verbose_name = 'Поставщик', on_delete=models.CASCADE, default=Supplier)
   options_list = (
       ('S', 'Small'),
       ('M', 'Medium'),
       ('L', 'Large'),
   )
   options = models.CharField('Опции', max_length=1, choices=options_list, default='S')
   img = models.ImageField('Фото', default= '', upload_to='products_img')
   slug = models.SlugField(null=False, unique=True, default='')
   
   def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    
   def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs) 
        
   def __str__(self):
       return self.title
     
   class Meta:
      verbose_name = 'Товар'
      verbose_name_plural = 'Товары'
      
    
class Orders(models.Model):
   
   order_number = models.IntegerField('Номер Заказа', default=0)
   date = models.DateTimeField('Дата', default=timezone.now)
   name = models.CharField('Имя', max_length=15)
   surname = models.CharField('Фамилия', max_length=20)
   phone = models.CharField('Телефон', max_length=10)
   email = models.CharField('Email', max_length=20, default='')
   total = models.CharField('Сумма', default='0',max_length=100)
   goods = models.CharField('Товары',max_length =250, default='')
   
   def __str__(self):
       return f'Заказ №{self.order_number}'
   
   class Meta:
      verbose_name = 'Заказ'
      verbose_name_plural = 'Заказы'
   