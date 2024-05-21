from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



class Invoice(models.Model):    
    invoice_no = models.BigIntegerField(primary_key=True)    
    invoice_price = models.PositiveIntegerField()
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()


class Item(models.Model):
    item_noo = models.PositiveIntegerField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_price = models.PositiveIntegerField()

class copy(models.Model):
    item_noo = models.PositiveIntegerField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_price = models.PositiveIntegerField()


class Complain(models.Model):
    complain_no = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
    csr_no = models.CharField(max_length=255)
    invoice_no = models.ForeignKey(Invoice,on_delete=models.DO_NOTHING)
    item_no = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    item_qty = models.PositiveIntegerField()
    recieved_qty = models.PositiveIntegerField(default=0)
    returned_qty = models.PositiveIntegerField(default=0)
    reason = models.CharField(max_length=255)
    notes = models.TextField()
    grn = models.CharField(max_length=255,default=1)
    status=models.CharField(max_length=255,default=1)


class CustomerInvoice(models.Model):
    c_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    invoice_no = models.ForeignKey(Invoice,on_delete=models.DO_NOTHING)


class antena(models.Model):
    invoice_no = models.ForeignKey(Invoice,on_delete=models.DO_NOTHING)
    item_no = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    item_qty = models.PositiveIntegerField()
    item_price = models.PositiveIntegerField()

    
class Employee(models.Model):
    emp_id = models.CharField(max_length=255,primary_key=True)
    emp_name = models.CharField(max_length=255)
    emp_password =  models.CharField(max_length=255)

class customerservice(models.Model):
    csr_no = models.CharField(max_length=255)
    emp_no = models.CharField(max_length=255)

class employeecustomer(models.Model):
    csr_no = models.ForeignKey(customerservice,on_delete=models.DO_NOTHING)
    complain_no = models.ForeignKey(Complain,default=1,on_delete=models.DO_NOTHING)

class custemp(models.Model):
     csr_no = models.ForeignKey(customerservice,on_delete=models.DO_NOTHING)
     c_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)

class complainimages(models.Model):
    complain_no = models.ForeignKey(Complain,default=1,on_delete=models.DO_NOTHING)
    f_path=models.CharField(max_length=255)
    
class docs(models.Model):
    complain_no = models.ForeignKey(Complain,default=1,on_delete=models.DO_NOTHING)
    in_path=models.CharField(max_length=255)
    eawaybill_path=models.CharField(max_length=255)

class errornumbers(models.Model):
    complain_no = models.ForeignKey(Complain,default=1,on_delete=models.DO_NOTHING)
    ser_no =models.PositiveIntegerField()
    ter_no=models.PositiveIntegerField()
    der_no=models.PositiveIntegerField()
    notes = models.TextField()

class track(models.Model):
    row = models.IntegerField(primary_key=True)
    hoos = models.IntegerField(default=0)