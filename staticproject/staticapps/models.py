from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=250)
    imge=models.ImageField(upload_to='pics')
    desc=models.TextField()

def __str__(self):
    return self.name
class managment(models.Model):
    mngrname=models.CharField(max_length=100)
    qualif=models.CharField(max_length=80)
    imgmngr=models.ImageField(upload_to='pics')
    descr=models.TextField()
def __str__(self):
    return self.name