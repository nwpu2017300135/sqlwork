from django.db import models
# Create your models here.
class  user(models.Model):
    gender=(('male','男'),('female','女'),)
    name=models.CharField(max_length=100,unique=True)
    true_name=models.CharField(max_length=256)
    password=models.CharField(max_length=100)
    sex=models.CharField(max_length=100,choices=gender,default='男')
    e_mail=models.EmailField(unique=True)
    c_time=models.DateField( auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
