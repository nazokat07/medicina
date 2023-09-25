from django.db import models

class Client(models.Model):

    name = models.CharField('Full name', max_length=256)
    phone = models.IntegerField('Phone number')

    def __str__(self):
        return f'{self.name}'
    
class Blog(models.Model):

    title = models.CharField('Name', max_length=256)
    image = models.ImageField('Image')
    text = models.TextField('Text')
    date = models.DateField()

    def __str__(self):
        return f'{self.title}'
    
class Sponsor(models.Model):

    name = models.CharField('Name', max_length=256)
    image = models.ImageField('Image')
    
    def __str__(self):
        return f'{self.name}'









