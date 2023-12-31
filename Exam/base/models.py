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
    is_checked_out = models.BooleanField(default=False)
    _id = models.AutoField(editable=False,primary_key=True)

    def __str__(self):
        return str(self.name)

class GotGadgetPermission(models.Model):
    employee= models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True)
    permitted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.permitted_at)

class Gadgettrackinfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    employee = models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True)
    gadget = models.ForeignKey(Gadgets,on_delete=models.SET_NULL,null=True)
    checkout_at = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    return_at = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    is_returned= models.BooleanField(default=False)
    return_con = models.CharField(max_length=200,blank=True,null=True)
    last_chek_con=models.CharField(max_length=200,blank=True,null=True)
    _id=models.AutoField(editable=False,primary_key=True)
    
    def __str__(self):
        return str(self.created_at)

