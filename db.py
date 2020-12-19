from mongoengine import *
from mongoengine.context_managers import switch_collection
from tkinter import messagebox 
import re
from datetime import datetime

#connect('psv', alias='db1',username='psv',password='psv')
connect('psv', alias='db1',host='mongodb+srv://psv:psv@cluster0.npmrc.mongodb.net/psv?retryWrites=true&w=majority')

class item(Document):
    itemno = StringField(primary_key=True)
    #itemno = StringField(max_length=50)
    itemname = StringField(max_length=550)
    price=FloatField()
    meta = {'db_alias': 'db1'}

# class item_used(EmbeddedDocument):
#     itemno = StringField(max_length=20)
#     itemname = StringField(max_length=550)
#     meta = {'db_alias': 'db1'}

class bill_item1(EmbeddedDocument):    
    slno = IntField()
    itemno= StringField(max_length=20)
    itemname= StringField(max_length=550)    
    itemtype= StringField(max_length=50)  
    uom=StringField(max_length=10)
    qty=FloatField()
    price=FloatField()
    total=FloatField()
    
class bill(Document):
    vehicleno = StringField(max_length=20)
    mobileno= StringField(max_length=10)
    custname = StringField(max_length=50)
    custadd= StringField(max_length=200)
    vehicleinfo = StringField(max_length=100)
    kilometer = StringField(max_length=100)
    invoiceno= StringField(primary_key=True)
    items = ListField(EmbeddedDocumentField(bill_item1))
    date_created = DateTimeField()
    date_modified = DateTimeField()
    meta = {'db_alias': 'db1'}

def addnewItem(itemname, price):
    newitem = item(itemname=itemname)
    if len(newitem) <=0:
        newitem = item()
    itemno =  "I" + str(item.objects.count() +1 ).zfill(5)
    newitem.itemno = itemno
    newitem.itemname = itemname
    newitem.price = price
    newitem.save()
    return itemno


def finditem_price(itemname): 
    if len(itemname) > 0:  
        item_price = [i.price for i in item.objects(itemname=itemname)]
        if len(item_price) >0:
            if item_price[0] != None:
                return item_price[0]
    return 0.0

def db_update_item_price(itemno, itemname, itemprice):
    newitem = item(itemno=itemno)  
    if len(newitem) >0:
        if newitem.price==None:
            #print("None price")
            item.objects(itemname=itemname).delete()
            newitem = item()          
     
    itemno =  itemno
    newitem.itemno = itemno
    newitem.itemname = itemname
    newitem.price = itemprice
    newitem.save()

def finditem(search):   
    return [i.itemname for i in item.objects(itemname__icontains=search)]

def findinvoice(frmbill):
    invno= frmbill.txtbillno['text']
    invdetail=bill(invoiceno=invno) 
    #if len(invdetail) >0 :
    pass

def getbill_details(invno):
   return bill.objects(invoiceno=invno)

def savebill(frmbill):
    
    try:

        vehicleno = frmbill.txtvehicleno.get('1.0','end-1c')
        mobileno = frmbill.txtmobileno.get('1.0','end-1c')
        kilometer = frmbill.txtkilometer.get('1.0','end-1c')
        vehicleinfo = frmbill.txtvehicleinfo.get('1.0','end-1c')


        if len(vehicleno) <=0:        
            messagebox.showinfo("No Items","vehicle # is Mandatory")
            return False

        if len(mobileno) <=0:        
            messagebox.showinfo("No Items","Enter mobile #")
            return False

        if len(kilometer) <=0:        
            messagebox.showinfo("No Items","Enter Kilometer #")
            return False

        if len(vehicleinfo) <=0:        
            messagebox.showinfo("No Items","Enter Make / Model #")
            return False

        if len(frmbill.Scrolledtreeview1.get_children()) <=0:        
            messagebox.showinfo("No Items","No Items")
            return False
            
        invno = frmbill.txtbillno['text']    
    
        bill_list = bill()
        bill_list.vehicleno = frmbill.txtvehicleno.get('1.0','end-1c')
        bill_list.mobileno= frmbill.txtmobileno.get('1.0','end-1c')
        bill_list.custname = frmbill.txtcustomerno.get('1.0','end-1c')
        bill_list.custadd= frmbill.txtaddress.get('1.0','end-1c')
        bill_list.vehicleinfo = frmbill.txtvehicleinfo.get('1.0','end-1c')
        bill_list.kilometer = frmbill.txtkilometer.get('1.0','end-1c')
        bill_list.date_created = datetime.now()
        bill_list.date_modified = datetime.now()

        if len(invno) > 0:
            bill_list.invoiceno= invno
        else:
            bill_list.invoiceno = "INV" + str(bill.objects.count() +1 ).zfill(4)    

        bill_list.items=[]

        for child in frmbill.Scrolledtreeview1.get_children():   
            bill_item=bill_item1()        
            bill_item.slno=int(frmbill.Scrolledtreeview1.item(child)["values"][0])         
            bill_item.itemno = str(frmbill.Scrolledtreeview1.item(child)["values"][1])  
            bill_item.itemtype = str(frmbill.Scrolledtreeview1.item(child)["values"][2])  
            bill_item.itemname= frmbill.Scrolledtreeview1.item(child)["values"][3]  
            bill_item.uom=frmbill.Scrolledtreeview1.item(child)["values"][4]  
            bill_item.qty=float(frmbill.Scrolledtreeview1.item(child)["values"][5]) 
            bill_item.price=float(frmbill.Scrolledtreeview1.item(child)["values"][6]) 
            bill_item.total=float(frmbill.Scrolledtreeview1.item(child)["values"][7])
            bill_list.items.append(bill_item)

        bill_list.save()
        messagebox.showinfo("Create Invoice","Successfully created")

        frmbill.txtbillno['text']=bill_list.invoiceno
        
    except Exception as e:
        messagebox.showerror("Error occured","%s" % e)
disconnect(alias='db1')
