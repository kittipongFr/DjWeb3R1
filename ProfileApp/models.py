from django.db import models
import uuid
class Product:
    def __init__(self,id,name,brand,price,amount,made,total,discount,net):
        self.id = id
        self.name =name
        self.brand = brand
        self.price = price
        self.amount = amount
        self.made =made
        self.total=total
        self.discount = discount
        self.net = net

    def getInfo(self):
        return "Id:{0}, Name: {1}, Brand: {2}, Price:{3}, Net: {4} ".format(self.id,self.name,self.brand,self.price,self.made)

class Category(models.Model):
    name = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=200,default="")

    def __str__(self):
        return  self.name



class product(models.Model):

    pid = models.CharField(primary_key=True,max_length=13, default="P"+str(uuid.uuid4())[:12], editable=False)
    name = models.CharField(max_length=50,default="")
    brand = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return  self.pid+" : "+self.name+" : "+self.brand+" : "+str(self.price)+" : "+str(self.net)+" : "+str(self.net)+" : "+str(self.category)

import datetime
class Employee(models.Model):
    eid = models.CharField(max_length=13,default="")
    name = models.CharField(max_length=35,default="")
    surname = models.CharField(max_length=35,default="")
    address = models.CharField(max_length=100, default="")
    gender= models.BooleanField(default=True)
    birthdate= models.DateTimeField(default="")
    salary = models.FloatField(default=0.00)
    def __str__(self):
        return self.eid +" : "+self.name+" : "+self.surname

class GoodsCategory(models.Model):
    gc_name = models.CharField(max_length=35,default="")
    desc = models.CharField(max_length=35,default="")

    def __str__(self):
        return self.gc_name
class Goods(models.Model):
    gid = models.CharField(max_length=13,primary_key=True,default="")
    goodscategory = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=35,default="")
    brand = models.CharField(max_length=35,default="")
    model = models.CharField(max_length=35,default="")
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.CharField(max_length=100,default="")
    def __str__(self):
        return str(self.goodscategory)+" : "+self.name+" : "+str(self.price)


class Customer(models.Model):
    cid = models.CharField(max_length=13,primary_key=True,default="")
    name = models.CharField(max_length=35,default="")
    surname = models.CharField(max_length=35,default="")
    address = models.CharField(max_length=100,default="")
    telephone = models.CharField(max_length=10,default="")
    gender = models.BooleanField(default=True)
    carreer =models.CharField(max_length=35,default="")
    password = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.cid +" : "+self.name+" : "+self.surname
    def getGender(self):
        if self.gender == True:
            return 'ชาย'
        else:
            return 'หญิง'

class Order(models.Model):
    oid  = models.CharField(max_length=13,primary_key=True,default="")
    date = models.DateTimeField(auto_now_add = True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=None)
    status = models.CharField(max_length=1,default="")
    def __str__(self):
        return self.oid +" : "+str(self.date)+" : "+str(self.customer)+self.status

    def newOrderId(self):
        # ord-yymm-xxxxxx
        yy = str(datetime.date.today().strftime('%y'))
        mm = str(datetime.date.today().strftime('%m'))
        lastOrder = Order.objects.last()
        if lastOrder:
            lastId = int(lastOrder.oid[9:])
        else:
            lastId = 0
        id = str(lastId + 1)
        id = id.zfill(6)
        newId = "OD-" + yy + mm + id
        self.oid = newId
    def getStatus(self):
        if self.status == '1':
            return 'Wait for Confirm'
        elif self.status == '2':
            return 'Wait for Money Transfer'
        elif self.status == '3':
            return 'Wait for Money Accept'
        elif self.status == '4':
            return 'Wait for Product Send'
        elif self.status == '5':
            return 'C o m p l e t e'
        elif self.status == '6':
            return 'Order Cancel'
        elif self.status == '7':
            return 'Order Reject'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,default=None)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,default=None)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order) +" : "+str(self.goods)+" : "+str(self.price)+str(self.quantity)