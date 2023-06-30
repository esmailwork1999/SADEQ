from django.db import models

# Create your models here.


TYPES = ('1','architecture'),('2','advertising')

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='اسم الفئة')
    type = models.CharField(max_length=100,choices=TYPES,verbose_name='التصنيف')
    slug = models.SlugField(max_length=100)
    description = models.TextField(verbose_name='الوصف',blank=True,null=True)

    class Meta:
        verbose_name = 'الفئة'
        verbose_name_plural = 'الفئات'


    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان الصورة')
    image = models.ImageField(upload_to='images/',verbose_name='الصورة')
    type = models.CharField(max_length=100,choices=TYPES,verbose_name='التصنيف')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='الفئة')
    class Meta:
        verbose_name = 'الصورة'
        verbose_name_plural = 'الصور'
    def __str__(self):
        return self.title