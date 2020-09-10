from db import *

def update_form_main(top):  
    global frmbill 
    frmbill=top

def find_price(itemname):
    item_price = finditem_price(itemname)
    frmbill.txtprice.delete('1.0','end')
    if item_price !=0.0:
        frmbill.txtprice.insert('1.0',str(item_price))
    #print(str(item_price))


   
