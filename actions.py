
# updateUIAttributes(top, root) -- create_Toplevel1
# from actions import *

def focus_next_widget(event,obj):
    obj.focus()
    #print(obj)
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
    print("test")
    additem()

def find_return(event, obj):
    findbill()

def numberonly(event, obj):   
   

    if event.keycode ==8 or event.keycode== 46:
        return True

    if event.keycode < 48 or event.keycode > 57:
        return("break")

    if (len(obj.get('1.0','end-1c')) > 9):
        return("break")


def updateUIAttributes(top, root):
    print("test")
    global frmbill
    frmbill=top
    frmbill.btnadditem.configure(command=additem)

    frmbill.btnfind.configure(command=findbill)   
    frmbill.btnfind.bind('<Return>', lambda event, obj=frmbill.btnfind: find_return(event,obj))
    
    frmbill.btnprint.configure(command=printbill)
   
    frmbill.txtvehicleno.bind("<Return>", lambda event, obj=frmbill.txtvehicleno: widget_return(event,obj))
    frmbill.txtmobileno.bind("<Return>", lambda event, obj=frmbill.txtmobileno: widget_return(event,obj))
    frmbill.txtmobileno.bind("<KeyPress>", lambda event, obj=frmbill.txtmobileno: numberonly(event,obj))
    frmbill.txtvehicleno.bind("<Tab>", lambda event, obj=frmbill.txtmobileno: focus_next_widget(event, obj))
    frmbill.txtmobileno.bind("<Tab>", lambda event, obj=frmbill.btnfind: focus_next_widget(event, obj)) 

    frmbill.txtcustomerno.bind("<Return>", lambda event, obj=frmbill.txtcustomerno: widget_return(event,obj))

            
    frmbill.cboitemname.bind("<Return>", lambda event, obj=frmbill.cboitemname: widget_return(event,obj))
    frmbill.cboitemname.bind("<Tab>", lambda event, obj=frmbill.cbouom: focus_next_widget(event, obj)) 

    frmbill.cbouom.bind("<Return>", lambda event, obj=frmbill.cbouom: widget_return(event,obj))
    frmbill.cbouom.bind("<Tab>", lambda event, obj=frmbill.txtqty: focus_next_widget(event, obj)) 

    frmbill.txtqty.bind("<Return>", lambda event, obj=frmbill.txtqty: widget_return(event,obj))
    frmbill.txtqty.bind("<Tab>", lambda event, obj=frmbill.txtprice: focus_next_widget(event, obj)) 

    frmbill.txtprice.bind("<Return>", lambda event, obj=frmbill.txtprice: widget_return(event,obj))
    frmbill.txtprice.bind("<Tab>", lambda event, obj=frmbill.txttotal: focus_next_widget(event, obj)) 

    frmbill.txttotal.bind("<Return>", lambda event, obj=frmbill.txttotal: widget_return(event,obj))
    frmbill.txttotal.bind("<Tab>", lambda event, obj=frmbill.btnadditem: focus_next_widget(event, obj)) 

    frmbill.btnadditem.bind('<Return>', lambda event, obj=frmbill.btnfind: add_return(event,obj))
    
    #frmbill.txtmobileno.bind("<Tab>", lambda event, obj=frmbill.btnfind: focus_next_widget(event, obj))   

    items=['item1','item2','item3','item4']
    frmbill.cboitemname.configure(values=items)

    frmbill.Scrolledtreeview1["columns"] = ("slno", "itemno","itemname","uom","qty","price","total")
    frmbill.Scrolledtreeview1['show'] = 'headings'
    
    frmbill.Scrolledtreeview1.column("slno", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("itemno", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("itemname", width=300, anchor='c')
    frmbill.Scrolledtreeview1.column("uom", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("qty", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("price", width=2, anchor='c')
    frmbill.Scrolledtreeview1.column("total", width=2, anchor='c')		

    frmbill.Scrolledtreeview1.heading("slno", text="SlNo")
    frmbill.Scrolledtreeview1.heading("itemno", text="Itemno")
    frmbill.Scrolledtreeview1.heading("itemname", text="ItemName")
    frmbill.Scrolledtreeview1.heading("uom", text="UOM")
    frmbill.Scrolledtreeview1.heading("qty", text="QTY")
    frmbill.Scrolledtreeview1.heading("price", text="Price")
    frmbill.Scrolledtreeview1.heading("total", text="Total")
    frmbill.Scrolledtreeview1.bind("<Double-1>", OnDoubleClick)


def findbill():
    vehicleno=frmbill.txtvehicleno.get('1.0','end-1c')
    mobileno=frmbill.txtmobileno.get('1.0','end-1c')
    
    print(vehicleno)
    print(mobileno)

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


def OnDoubleClick(event):
    #print(event)

    

    item=frmbill.Scrolledtreeview1.identify('item',event.x,event.y)
    #item = frmbill.Scrolledtreeview1.selection()[0]
    #print("you clicked on", frmbill.Scrolledtreeview1.item(item,"values"))
    selitem=frmbill.Scrolledtreeview1.item(item,"values")


    frmbill.txtitemno.delete('1.0','end')
    frmbill.txtqty.delete('1.0','end')
    frmbill.txtprice.delete('1.0','end')
    frmbill.txttotal.delete('1.0','end')


    #print(selitem[0])
    frmbill.lblitemslno['text']=selitem[0]
    frmbill.txtitemno.insert('1.0',selitem[1])

    # frmbill.cboitemname.insert('1.0',selitem[2])
    # frmbill.cbouom.insert('1.0',selitem[3])

    frmbill.txtqty.insert('1.0',selitem[4])
    frmbill.txtprice.insert('1.0',selitem[5])
    frmbill.txttotal.insert('1.0',selitem[6])

from print import openprint

def printbill():
    openprint()
    
    
    #App = QApplication(sys.argv)
    #window = Window()
    #sys.exit(App.exec())

def additem():    
    #print("test")   
    # vehicleno=frmbill.txtvehicleno.get('1.0','end-1c')
    itemname= frmbill.cboitemname.get()
    uom = frmbill.cbouom.get()
    qty = frmbill.txtqty.get('1.0','end-1c')
    price = frmbill.txtprice.get('1.0','end-1c')
    total = frmbill.txttotal.get('1.0','end-1c')
    
    slno= len(frmbill.Scrolledtreeview1.get_children())+1
    values=[]
    values.append(slno)
    values.append("itemNo")
    values.append(itemname)
    values.append(uom)
    values.append(qty)
    values.append(price)
    values.append(total)
    t=tuple(values)
    #print(t)
    frmbill.Scrolledtreeview1.insert("",'end', iid=slno,text="L1",values=t)
    

    # print(itemname)
    # print(uom)
    # txtmobileno
    # btnfind

# def insert_data(self):
#     self.treeview.insert('', 'end', iid=self.iid,text="",values=())
#     self.iid = self.iid + 1
#     self.id = self.id + 
    
