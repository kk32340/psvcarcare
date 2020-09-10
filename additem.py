
from tkinter import *  
from tkinter import messagebox 
from db import *

def get_duple(frmbill):
    itemname= frmbill.cboitemname.get()

    #print(itemname)

    itemtype= frmbill.cboitemtype.get()
    uom = frmbill.cbouom.get()
    qty = frmbill.txtqty.get('1.0','end-1c')
    if len(qty) ==0:
        qty="0.0"        
    price = frmbill.txtprice.get('1.0','end-1c')
    if len(price) ==0:
        price="0.0"

    qtyval=float(qty)
    priceval=float(price)

    priceval = float("{:.2f}".format(priceval))

    totalval = float(qtyval * priceval)

    totalval = float("{:.2f}".format(totalval))

    #print(priceval)
      
    slno= len(frmbill.Scrolledtreeview1.get_children())+1

    slnoupd=frmbill.lblitemslno['text']
    if len(slnoupd) > 0:
        slno = int(slnoupd)
    values=[]
    if slno > 0:
        values.append(slno)

    item_added = item.objects(itemname=itemname)

    if len(item_added) > 0:
        values.append(item_added[0].itemno)

    if len(itemtype) > 0:
        values.append(itemtype)

    if len(itemname) > 0:
        values.append(itemname)

    
    if len(uom) > 0:
        values.append(uom)
    if qtyval > 0:        
        values.append(qtyval)
    if priceval > 0:
        values.append(priceval)
    if totalval > 0:
        values.append(totalval)

    #print(values)

    return tuple(values)


def get_inv_duple_data(data):    
    list=[]
    if len(data) > 0:
        for i in data:
            #print(i.date_created.strftime("%m/%d/%Y %H:%M"))
            dateval=""
            if i.date_created == None:
                dateval =""
            else:
                dateval= i.date_created.strftime("%m/%d/%Y")
            list.append((i.invoiceno,dateval, i.vehicleno, i.custname))
        return list
    else:
        return []

def get_inv_duple(vehicleno, mobileno):    
    if len(vehicleno) > 0:
        data = bill.objects(vehicleno__icontains=vehicleno)
        return get_inv_duple_data(data)
    else:
        data = bill.objects(mobileno__icontains=mobileno)
        return get_inv_duple_data(data)

def get_item_duple(item_list):   
    list=[] 
    for i in item_list:
        list.append((i.slno, i.itemno, i.itemtype, i.itemname, i.uom, i.qty, i.price, i.total))
    return list




def validateitem(frmbill):
    validated=False

    itemname= frmbill.cboitemname.get()
    itemtype= frmbill.cboitemtype.get()
    uom = frmbill.cbouom.get()
    qty = frmbill.txtqty.get('1.0','end-1c')
    if len(qty) ==0:
        qty="0"        
    price = frmbill.txtprice.get('1.0','end-1c')
    if len(price) ==0:
        price="0.0"

    qtyval=float(qty)
    priceval=float(price)
    totalval = float(qtyval * priceval)
      
    slno= len(frmbill.Scrolledtreeview1.get_children())+1
    slnoupd=frmbill.lblitemslno['text']
    if len(slnoupd) > 0:
        slno = int(slnoupd)
    values=[]
    if slno > 0:
        values.append(slno)

    item_added = item.objects(itemname=itemname)
    
    if len(item_added) > 0:
        values.append(item_added[0].itemno)
    
    if len(itemtype) > 0:
        values.append(itemtype)

    if len(itemname) > 0:
        values.append(itemname)
    if len(uom) > 0:
        values.append(uom)
    if qtyval > 0:        
        values.append(qtyval)
    if priceval > 0:
        values.append(priceval)
    if totalval > 0:
        values.append(totalval)
    t=tuple(values)   
    # print(t) 
    # print(len(t)) 
    if len(t) < 8:
        return validated
    return True
        #messagebox.showwarning("enter all details","Warning")
  
      

    
