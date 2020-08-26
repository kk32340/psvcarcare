class billitem():
    def __init__(self, slno, billno, itemname, uom, qty, price, total):
        self.slno=slno
        self.billno=billno
        self.itemname=itemname
        self.uom=uom
        self.qty=qty
        self.price=price
        self.total=total

class billitems():
    def __init__(self):
        self.data=[]

    def  additem(item):
        self.data.append(item)