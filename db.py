from mongoengine import *
from mongoengine.context_managers import switch_collection
from tkinter import messagebox 
import re
from datetime import datetime

connect('psv', alias='db1',username='psv',password='psv')

class item(Document):
    itemno = StringField(max_length=20)
    itemname = StringField(max_length=100)
    meta = {'db_alias': 'db1'}

# class item_used(EmbeddedDocument):
#     itemno = StringField(max_length=20)
#     itemname = StringField(max_length=100)
#     meta = {'db_alias': 'db1'}

class bill_item1(EmbeddedDocument):    
    slno = IntField()
    itemno= StringField(max_length=20)
    itemname= StringField(max_length=150)    
    itemtype= StringField(max_length=50)  
    uom=StringField(max_length=10)
    qty=IntField()
    price=FloatField()
    total=FloatField()
    
class bill(Document):
    vehicleno = StringField(max_length=20)
    mobileno= StringField(max_length=10)
    custname = StringField(max_length=50)
    custadd= StringField(max_length=200)
    vehicleinfo = StringField(max_length=100)
    invoiceno= StringField(primary_key=True)
    items = ListField(EmbeddedDocumentField(bill_item1))
    date_created = DateTimeField()
    date_modified = DateTimeField()
    meta = {'db_alias': 'db1'}

def addnewItem(itemname):
    newitem = item(itemname=itemname)
    if len(newitem) <=0:
        newitem = item()
    itemno =  "I" + str(item.objects.count() +1 ).zfill(5)
    newitem.itemno = itemno
    newitem.itemname = itemname
    newitem.save()
    return itemno

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
    
    validated = True

    vehicleno = frmbill.txtvehicleno.get('1.0','end-1c')
    mobileno = frmbill.txtmobileno.get('1.0','end-1c')
    
    if len(vehicleno) <=0:
        validated = False
        messagebox.showinfo("No Items","vehicle # is Mandatory")

    if len(mobileno) <=0:
        validated = False
        messagebox.showinfo("No Items","Enter mobile #")

    if len(frmbill.Scrolledtreeview1.get_children()) <=0:
        validated = False
        messagebox.showinfo("No Items","No Items")

    if validated==False:
        return False


    invno = frmbill.txtbillno['text']    
   
    bill_list = bill()
    bill_list.vehicleno = frmbill.txtvehicleno.get('1.0','end-1c')
    bill_list.mobileno= frmbill.txtmobileno.get('1.0','end-1c')
    bill_list.custname = frmbill.txtcustomerno.get('1.0','end-1c')
    bill_list.custadd= frmbill.txtaddress.get('1.0','end-1c')
    bill_list.vehicleinfo = frmbill.txtvehicleinfo.get('1.0','end-1c')
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
        bill_item.qty=int(frmbill.Scrolledtreeview1.item(child)["values"][5]) 
        bill_item.price=float(frmbill.Scrolledtreeview1.item(child)["values"][6]) 
        bill_item.total=float(frmbill.Scrolledtreeview1.item(child)["values"][7])
        bill_list.items.append(bill_item)

    bill_list.save()
    messagebox.showinfo("Create Invoice","Successfully created")

    frmbill.txtbillno['text']=bill_list.invoiceno

disconnect(alias='db1')
