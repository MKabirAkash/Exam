from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    position = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    _id = models.AutoField(editable=False,primary_key=True)

    def __str__(self):
        return str(self.name)



class Gadgets(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    present_con = models.CharField(max_length=200,blank=True,null=True)
    last_chek_con=models.CharField(max_length=200,blank=True,null=True)
    is_checked_out = models.BooleanField(default=False)
    last_checkout_at = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    last_return_at = models.DateTimeField(auto_now_add=False)
    _id = models.AutoField(editable=False,primary_key=True)

    def __str__(self):
        return str(self.name)
