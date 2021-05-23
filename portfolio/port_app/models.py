from django.db import models
class Services(models.Model):
    name=models.CharField(max_length=100,unique=True,verbose_name="service name")
    desc=models.TextField(blank=True,verbose_name='service desc')
    image=models.ImageField(upload_to='services',verbose_name='image')
    class Meta:
        verbose_name='service'
        verbose_name_plural='task'
    def __str__(self):
        return self.name

class MyModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    msg=models.TextField()