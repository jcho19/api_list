from django.db import models

#category of public API
class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250, unique=True)
    owner = models.ForeignKey('auth.User',
                              related_name='categories', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created', )
        
#information on public API (name, website, description, etc.)     
class Api(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250, unique=True)
    website = models.URLField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='apis', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',
                              related_name='apis', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created', )
