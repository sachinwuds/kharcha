from django.db import models

# Create your models here.
class Expenses(models.Model):
    token = models.CharField(max_length=254, blank=True,  null=True)
    itemname = models.CharField(max_length=254, blank=True,  null=True)
    price = models.CharField(max_length=254, blank=True,  null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True,)
    
    def __str__(self):
        return str(self.itemname)
    
    class Meta:
        db_table = 'expenses'