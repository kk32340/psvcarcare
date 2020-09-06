
# updateUIAttributes(top, root) -- vp_start_gui
# from actions import *

import psv_support
from additem import *
from print import openprint
from tkinter import messagebox 
from mongoengine import *
from mongoengine.context_managers import switch_collection
from db import *
from psv import *
from printdocument import *

def focus_next_widget(event,obj):
    obj.focus()
    #print(obj)
    return("break")

def focus_next_widget1(event, source, obj):
    source.unpost_listbox()
    obj.focus()
    return("break")

def widget_return(event, obj):
    # value=obj.get('1.0','end-1c')
    # obj.delete('1.0','end')
    # obj.insert('1.0',value)
    return("break")

    #print("test")
    # frmbill.btnfind.invoke()
    # return("break")

def add_return(event, obj):    
    additem()

def find_return(event, obj):
    window = tk.Toplevel(root)
    #findbill()

def numberonly(event, obj):   

    if event.keycode ==8 or event.keycode== 46:
        return True

    if event.keycode < 48 or event.keycode > 57:
        return("break")

    if (len(obj.get('1.0','end-1c')) > 9):
        return("break")


def numbers1 (event, obj):
    v = event.char
    
    try:
        v = int(v)

        # val=int(obj.get('1.0','end-1c'))
        # frmbill.txttotal.configure(text='test1')

    except ValueError:
        if v!="\x08" and v!="":
            return "break"

def floatonly (event, obj):
    v = event.char    
    try:

        # if obj.get('1.0','end-1c').count('.') > 1:
        #     return "break"

        if v==".":
            return True
        v = float(v)
    except ValueError:
        if v!="\x08" and v!="":
            return "break"

def floatonly1 (event, obj):
    v = event.char
    val=obj.get('1.0','end-1c')
    #print(val)
    #print(validate(obj.get('1.0','end-1c')))

    try:
        v = float(val)
        if len(val) >0:
            #print("v is : ")
            #print(v)
            return("break")
        else:
            return True
    except ValueError:
        #if v!="\x08" and v!="":
        return("break")


def check(event):
    text = event.widget.get()
    #print('text:', text)

    parts = text.split('.')
    parts_number = len(parts)

    if parts_number > 2:
        print('too much dots')

    if parts_number > 1 and parts[1]: # don't check empty string
        if not parts[1].isdecimal() or len(parts[1]) > 2:
            print('wrong second part')

    if parts_number > 0 and parts[0]: # don't check empty string
        if not parts[0].isdecimal() or len(parts[0]) > 8:
            print('wrong first part')

def validate(string):
    regex = re.compile(r"(\+|\-)?[0-9,]*$")
    result = regex.match(string)
    return (string == ""
            or (string.count('+') <= 1
                and string.count('-') <= 1
                and string.count(',') <= 1
                and result is not None
                and result.group(0) != ""))
    
def on_validate(P):
    return validate(P)    

def updateUIAttributes(top, root):  
    global frmbill
    global parentroot
    frmbill=top
    parentroot = root
    frmbill.btnadditem.configure(command=additem)
    frmbill.btnclear.configure(command=clearitem)
    frmbill.btnsave.configure(command=saveitem)
    frmbill.btnnewbill.configure(command=newitem)
    frmbill.btndelete.configure(command=del_treeview_item)
        
    frmbill.btnfind.configure(command=findbill)   
    frmbill.btnfind.bind('<Return>', lambda event, obj=frmbill.btnfind: find_return(event,obj))
    
    frmbill.btnprint.configure(command=printbill)
   
    frmbill.txtvehicleno.bind("<Return>", lambda event, obj=frmbill.txtvehicleno: widget_return(event,obj))
    frmbill.txtmobileno.bind("<Return>", lambda event, obj=frmbill.txtmobileno: widget_return(event,obj))
    frmbill.txtmobileno.bind("<KeyPress>", lambda event, obj=frmbill.txtmobileno: numberonly(event,obj))
    frmbill.txtvehicleno.bind("<Tab>", lambda event, obj=frmbill.txtmobileno: focus_next_widget(event, obj))
    frmbill.txtmobileno.bind("<Tab>", lambda event, obj=frmbill.btnfind: focus_next_widget(event, obj)) 

    frmbill.txtbillno.configure(text='')

    frmbill.txtcustomerno.bind("<Tab>", lambda event, obj=frmbill.txtaddress: focus_next_widget(event, obj))
    frmbill.txtaddress.bind("<Tab>", lambda event, obj=frmbill.txtvehicleinfo: focus_next_widget(event, obj))
    frmbill.txtvehicleinfo.bind("<Tab>", lambda event, obj=frmbill.cboitemname: focus_next_widget(event, obj))

    frmbill.txtcustomerno.bind("<Return>", lambda event, obj=frmbill.txtcustomerno: widget_return(event,obj))

    frmbill.lblitemslno['text']=""

    frmbill.cboitemtype.bind("<Return>", lambda event, obj=frmbill.cboitemtype: widget_return(event,obj))
    frmbill.cboitemtype.bind("<Tab>", lambda event, obj=frmbill.cboitemname: focus_next_widget(event, obj)) 
    frmbill.cboitemtype.configure(textvariable=psv_support.varcboitemtype)

    # frmbill.cboitemname.bind("<Return>", lambda event, obj=frmbill.cboitemname: widget_return(event,obj))
    frmbill.cboitemname.bind("<Tab>", lambda event, obj1=frmbill.cboitemname, obj=frmbill.cbouom: focus_next_widget1(event,obj1, obj)) 
    # frmbill.cboitemname.configure(textvariable=psv_support.varcboitemname)

    frmbill.cbouom.bind("<Return>", lambda event, obj=frmbill.cbouom: widget_return(event,obj))
    frmbill.cbouom.bind("<Tab>", lambda event, obj=frmbill.txtqty: focus_next_widget(event, obj)) 
    frmbill.cbouom.configure(textvariable=psv_support.varcbouom)
    uom_value_list = ['NOS','KG','LTR']
    frmbill.cbouom.configure(values=uom_value_list)
    frmbill.cbouom.configure(state='readonly')

    frmbill.txtqty.bind("<Return>", lambda event, obj=frmbill.txtqty: widget_return(event,obj))
    frmbill.txtqty.bind("<Tab>", lambda event, obj=frmbill.txtprice: focus_next_widget(event, obj))
   
    frmbill.txtqty.bind("<KeyPress>", lambda event, obj=frmbill.txtqty: numbers1(event,obj))
    frmbill.txtprice.bind("<KeyPress>", lambda event, obj=frmbill.txtprice: floatonly(event,obj))

    frmbill.txtprice.bind("<Return>", lambda event, obj=frmbill.txtprice: widget_return(event,obj))
    frmbill.txtprice.bind("<Tab>", lambda event, obj=frmbill.txttotal: focus_next_widget(event, obj)) 

    frmbill.txttotal.bind("<Return>", lambda event, obj=frmbill.txttotal: widget_return(event,obj))
    frmbill.txttotal.bind("<Tab>", lambda event, obj=frmbill.btnadditem: focus_next_widget(event, obj)) 

    frmbill.btnadditem.bind('<Return>', lambda event, obj=frmbill.btnfind: add_return(event,obj))
    frmbill.btnclear.bind('<Return>', lambda event, obj=frmbill.btnclear: clearitem(event,obj))


    # items=['item1','item2','item3','item4']
    # frmbill.cboitemname.configure(values=items)

    frmbill.Scrolledtreeview1["columns"] = ("slno", "itemno","itemtype","itemname","uom","qty","price","total")
    frmbill.Scrolledtreeview1['show'] = 'headings'
    
    frmbill.Scrolledtreeview1.column("slno", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("itemno", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("itemtype", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("itemname", width=300, anchor='c')
    frmbill.Scrolledtreeview1.column("uom", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("qty", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("price", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("total", width=2, anchor='c')		

    frmbill.Scrolledtreeview1.heading("slno", text="SlNo")
    frmbill.Scrolledtreeview1.heading("itemno", text="Itemno")
    frmbill.Scrolledtreeview1.heading("itemtype", text="Itemtype")
    frmbill.Scrolledtreeview1.heading("itemname", text="ItemName")
    frmbill.Scrolledtreeview1.heading("uom", text="UOM")
    frmbill.Scrolledtreeview1.heading("qty", text="QTY")
    frmbill.Scrolledtreeview1.heading("price", text="Price")
    frmbill.Scrolledtreeview1.heading("total", text="Total")
    frmbill.Scrolledtreeview1.bind("<Double-1>", OnDoubleClick)


def findbill():
    vehicleno=frmbill.txtvehicleno.get('1.0','end-1c')
    mobileno=frmbill.txtmobileno.get('1.0','end-1c')

    if len(vehicleno) <= 0 and len(mobileno) <=0:       
        messagebox.showwarning("Find Invoice","Enter vehicle # or Mobile #")
        frmbill.txtvehicleno.focus()
        return False

    x=parentroot.winfo_rootx()
    y=parentroot.winfo_rooty()
    #h=parentroot.winfo_height()
    window = tk.Toplevel(parentroot)
    #window.geometry("200x200") 
    window.geometry("+%d+%d" % (x+450,
                          y+70
                         )
             ) 
    window.geometry("380x200")
    window.update()
    window.resizable(0,0)
    window.title("Invoice List")
    window.attributes("-toolwindow", 1)

    Scrolledtreeview1 = ScrolledTreeView(window)    
    Scrolledtreeview1.pack(side="top", fill="both", expand=True, padx=0, pady=0)

    Scrolledtreeview1["columns"] = ("invoiceno","date_modified", "vehicleno","custname")
    Scrolledtreeview1['show'] = 'headings'
    
    Scrolledtreeview1.column("invoiceno", width=2, anchor='c')
    Scrolledtreeview1.column("date_modified", width=2, anchor='c')
    Scrolledtreeview1.column("vehicleno", width=2, anchor='c')
    Scrolledtreeview1.column("custname", width=2, anchor='c')

    Scrolledtreeview1.heading("invoiceno", text="Inv.No")
    Scrolledtreeview1.heading("date_modified", text="Inv.Date")
    Scrolledtreeview1.heading("vehicleno", text="Vehicleno")
    Scrolledtreeview1.heading("custname", text="Name")
    
    #Scrolledtreeview1.bind("<Double-1>", invDoubleClick(Scrolledtreeview1))
    Scrolledtreeview1.bind("<Double-1>", lambda event, obj=Scrolledtreeview1: invDoubleClick(event, obj)) 

    values=get_inv_duple(vehicleno, mobileno)              
    #print(values)

    for i in values:
        Scrolledtreeview1.insert("",'end', iid=str(i[0]),text="L1",values=i)


def invDoubleClick(event, treeview):
    #print(event)
    item=treeview.identify('item',event.x,event.y)    
    #print(item)
    loadinv(item)
    #selitem=treeview.identify.item(item,"values")

def newitem():
    # frmbill.txtvehicleno.delete('1.0','end')    
    #frmbill.txtmobileno.delete('1.0','end')    
    frmbill.txtbillno['text']=""
    #frmbill.txtcustomerno.delete('1.0','end')    
    #frmbill.txtaddress.delete('1.0','end')    
    #frmbill.txtvehicleinfo.delete('1.0','end')
    clearitem()
    frmbill.Scrolledtreeview1.delete(*frmbill.Scrolledtreeview1.get_children())

def loadinv(invno):
    data_list = bill.objects(invoiceno=invno)
    data = data_list[0]
    #print(data[0])
    
    if len(data) > 0:
        frmbill.txtvehicleno.delete('1.0','end')
        frmbill.txtvehicleno.insert('1.0',data.vehicleno)

        frmbill.txtmobileno.delete('1.0','end')
        frmbill.txtmobileno.insert('1.0',data.mobileno)

        frmbill.txtbillno['text']=data.invoiceno

        frmbill.txtcustomerno.delete('1.0','end')
        frmbill.txtcustomerno.insert('1.0',data.custname)

        frmbill.txtaddress.delete('1.0','end')
        frmbill.txtaddress.insert('1.0',data.custadd)

        frmbill.txtvehicleinfo.delete('1.0','end')
        frmbill.txtvehicleinfo.insert('1.0',data.vehicleinfo)
        # print(data.items)
        # return False
        values = get_item_duple(data.items)
        
        frmbill.Scrolledtreeview1.delete(*frmbill.Scrolledtreeview1.get_children())
        for i in values:
            frmbill.Scrolledtreeview1.insert("",'end', iid=str(i[0]),text="L1",values=i)


# btnnewbill
# btnmodifybill
# txtbillno
# txtcustomerno
# txtaddress
# txtvehicleinfo
# txtitemno
# lblitemslno
# cboitemname
# cbouom
# txtqty
# txtprice
# txttotal
# btnprint
# def update(self):
#     for idx, node in enumerate(self.treeview.get_children()):
#         self.tree.item(node, text="Updated_Item_" + str(idx))

def del_treeview_item():
    slno=frmbill.lblitemslno['text']
    if len(slno) > 0:        
        for i in frmbill.Scrolledtreeview1.get_children():
            if slno == i:
                frmbill.Scrolledtreeview1.delete(i)


def additem():
    itemname=frmbill.cboitemname.get_value()
    if len(itemname) > 0:
        if len(item.objects(itemname=itemname)) <=0:        
            if messagebox.askyesno("New Item","Item does not exists \n, do you want to create new item?"):
                addnewItem(itemname)    

    val = validateitem(frmbill)
    #print(itemname)
    #print(val)

    if validateitem(frmbill):        
        slnoupd=frmbill.lblitemslno['text']
        #itemno=frmbill.txtitemno.get('1.0','end-1c')
        #print("item No")
        #print(itemno)
        #if len(itemno)==0:
         #   addnewItem(frmbill.cboitemname.get())            
            #frmbill.txtitemno.insert('1.0',itemnoadded)

        #messagebox.showinfo(str(len(itemno)))

        if slnoupd !="":
            if frmbill.Scrolledtreeview1.exists(slnoupd)==True:
                values=get_duple(frmbill)  
                #print(values)  
                #messagebox.showwarning("item exists", "item exists")
                frmbill.Scrolledtreeview1.item(slnoupd,values=values)
                clearitem()
                return True
        else:
            values=get_duple(frmbill)              
            #frmbill.cboitemname.set("")
            frmbill.Scrolledtreeview1.insert("",'end', iid=str(values[0]),text="L1",values=values)
            clearitem()
    else:
        messagebox.showwarning("enter all details","Invalid item")  


def saveitem():
    savebill(frmbill)

def OnDoubleClick(event):
    #print(event)
    item=frmbill.Scrolledtreeview1.identify('item',event.x,event.y)
    #item = frmbill.Scrolledtreeview1.selection()[0]
    #print("you clicked on", frmbill.Scrolledtreeview1.item(item,"values"))
    selitem=frmbill.Scrolledtreeview1.item(item,"values")
    #print(selitem)

    frmbill.txtitemno.delete('1.0','end')
    frmbill.txtqty.delete('1.0','end')
    frmbill.txtprice.delete('1.0','end')
    frmbill.txttotal.delete('1.0','end')

    #print(selitem[0])
    frmbill.lblitemslno['text']=selitem[0]
    frmbill.txtitemno.configure(state='normal')
    frmbill.txtitemno.delete('1.0','end')
    frmbill.txtitemno.insert('1.0',selitem[1])
    #frmbill.txtitemno.configure(state='disabled')

    # frmbill.cboitemname.insert('1.0',selitem[2])
    # frmbill.cbouom.insert('1.0',selitem[3])

    psv_support.varcboitemtype.set(selitem[2])
    #psv_support.varcboitemname.set(selitem[3])
    frmbill.cboitemname.set_value(selitem[3])
    psv_support.varcbouom.set(selitem[4])

    frmbill.txtqty.insert('1.0',selitem[5])
    frmbill.txtprice.insert('1.0',selitem[6])
    frmbill.txttotal.insert('1.0',selitem[7])

def printbill():
    inv=frmbill.txtbillno['text']
    if len(inv) >0:
        #details=getbill_details(inv)
        details = bill.objects(invoiceno=inv)                        
        printstr=getdocument(details[0])
        openprint(printstr)
    else:
        messagebox.showwarning("Print","Save Invoice before print")
        

connect('psv', alias='db1',username='psv',password='psv')  

def clearitem():
    frmbill.lblitemslno['text']=""

    frmbill.txtitemno.configure(state='normal')
    frmbill.txtitemno.delete('1.0','end')   
    frmbill.txtitemno.configure(state='disabled')

    frmbill.txtqty.delete('1.0','end')
    frmbill.txtprice.delete('1.0','end')
    frmbill.txttotal.delete('1.0','end')
    psv_support.varcboitemtype.set("")
    #psv_support.varcboitemname.set("")
    frmbill.cboitemname.set_value("")
    psv_support.varcbouom.set("")

    
