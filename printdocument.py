from db import *

def getdocument(details):
    bill=""
    bill += "PSP"
    bill += "\n" + "CAR CARE"
    bill += "\n" + "1223/6B, BY-PASS ROAD"
    bill += "\n" + "SHANMUGANATHI, PALANI-624 602"
    bill += "\n" + "EMAIL:pspcarcare@gmail.com                                                                  INVOICE NO:" + details.invoiceno
    bill += "\n" + "PHONE NO: 9944429143, 9787703040                                                    INVOICEDATE:" + details.date_modified.strftime("%m/%d/%Y %H:%M")
    bill += "\n"
    bill += "\n"
    bill += "{0:<10}".format("S.No")
    bill += "{0:<65}".format("ITEM DESCRIPTION") 
    bill += "{0:<10}".format("UNIT") 
    bill += "{0:<15}".format("QUANTITY") 
    bill += "{0:<15}".format("AMOUNT") 
    bill += "{0:<15}".format("TOTAL") 
    bill += "\n"
    bill += "---------------------------------------------------------------------------------------------------------------------------------------------------------"
    bill += "\n"
    gtotal=0
    for i in details.items:
        gtotal += i.total
        bill += "{0:^10}".format(str(i.slno))
        bill += "{0:<80}".format(i.itemname) 
        bill += "{0:<10}".format(str(i.uom)) 
        bill += "{0:>15}".format(str(i.qty)) 
        bill += "{0:>15}".format(str(i.price)) 
        bill += "{0:>15}".format(str(i.total)) 
        bill += "\n"
    bill += "---------------------------------------------------------------------------------------------------------------------------------------------------------"
    bill += "\n"
    bill += "{0:>138}".format("Total:")
    bill += "{0:>15}".format(str(gtotal))
    bill += "\n"
    bill += "---------------------------------------------------------------------------------------------------------------------------------------------------------"
    
    return bill