from mongoengine import *
from mongoengine.context_managers import switch_collection


connect('psv', alias='db1',username='psv',password='psv')




class bill_item1(EmbeddedDocument):    
    slno = IntField()
    itemno= StringField(max_length=20)
    itemname= StringField(max_length=150)
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
    invoiceno= StringField(max_length=10)
    items = ListField(EmbeddedDocumentField(bill_item1))
    meta = {'db_alias': 'db1'}

def savebill(frmbill):

    
    bill_list=bill()

    bill_list.vehicleno = frmbill.txtvehicleno.get('1.0','end-1c')
    bill_list.mobileno= frmbill.txtmobileno.get('1.0','end-1c')
    bill_list.custname = frmbill.txtcustomerno.get('1.0','end-1c')
    bill_list.custadd= frmbill.txtaddress.get('1.0','end-1c')
    bill_list.vehicleinfo = frmbill.txtvehicleinfo.get('1.0','end-1c')
    #bill_list.invoiceno= frmbill.txtmobileno.get('1.0','end-1c')


    for child in frmbill.Scrolledtreeview1.get_children():   
        bill_item=bill_item1()
        bill_item.slno=int(frmbill.Scrolledtreeview1.item(child)["values"][0]) 
        bill_item.itemno=frmbill.Scrolledtreeview1.item(child)["values"][1] 
        bill_item.itemname=frmbill.Scrolledtreeview1.item(child)["values"][2]  
        bill_item.uom=frmbill.Scrolledtreeview1.item(child)["values"][3]  
        bill_item.qty=int(frmbill.Scrolledtreeview1.item(child)["values"][4]) 
        bill_item.price=float(frmbill.Scrolledtreeview1.item(child)["values"][5]) 
        bill_item.total=float(frmbill.Scrolledtreeview1.item(child)["values"][6]) 

        bill_list.items.append(bill_item)

    bill_list.save()

disconnect(alias='db1')
