def getdocument(details):  
    print(details)
    bill_item = details.items      
    params={}
    params["i1"]="item1"
    params["i2"]="item2"
    params["i3"]="item3"
    params["i4"]="item4"
    params["invno"]="3"
    params["invoicedate"]="26/08/2020"

    bill="""    
    PSP
    CAR CARE
    1223/6B, BY-PASS ROAD
    SHANMUGANATHI, PALANI-624 602
    EMAIL:pspcarcare@gmail.com                                                                  INVOICE NO: {invoiceno}
    PHONE NO: 9944429143, 9787703040                                                    INVOICEDATE:{invoicedate}
        
    S.No                     ITEM DESCRIPTION                                            QUANTITY 	UNIT    	AMOUNT
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """.format(**params)

    for item in bill_item:
        bill += item.slno + "    "
        bill += item.itemname + "    "
        bill += item.uom + "    "
        bill += item.qty + "    "
        bill += item.price + "    "

    # for item in range(20)
    # items=""
    # items += replicate(" ",3)

    return bill

def replicate(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]
