class document_item:
    def __init__(self,slno,itemno, itemname, qty, uom, price, total):
        self.slno=slno
        self.itemno=itemno
        self.itemname=itemname
        self.qty=qty
        self.uom=uom
        self.price=price
        self.total=total



def getdocument():        
    params={}
    params["i1"]="item1"
    params["i2"]="item2"
    params["i3"]="item3"
    params["i4"]="item4"
    params["invno"]="3"
    params["invoicedate"]="26/08/2020"

    list1=[]
    #item=document_item(1,"item1","itemname1",10,"nos",)

    bill="""
    PSP
    CAR CARE
    1223/6B, BY-PASS ROAD
    SHANMUGANATHI, PALANI-624 602
    EMAIL:pspcarcare@gmail.com                                                                  INVOICE NO: {invno}
    PHONE NO: 9944429143, 9787703040                                                    INVOICEDATE:{invoicedate}
        
    S.No                     ITEM DESCRIPTION                                            QUANTITY 	UNIT    	AMOUNT
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """.format(**params)

    # for item in range(20)
    # items=""
    # items += replicate(" ",3)

    return bill

def replicate(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]
