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
        
        # bill += "%50s" % i.itemname.upper()
        # bill += "%10s" % i.uom.upper()

        # i_name = "{0:<80}".format(i.itemname.upper())
        # i_uom = "{0:<10}".format(str(i.uom.upper())) 

        # print(len(i_name)) 
        # print(len(i_uom)) 

        bill += "{0:<50}".format(i.itemname.upper())  + "{0:<10}".format(str(i.uom.upper()))
        #bill += "{0:<10}".format(str(i.uom.upper())) 

        # name = i.itemname.upper()
        # name = name + repeat_to_length(" ",50-len(name))
        # bill += name

        # uom = i.uom.upper()
        # uom = uom + repeat_to_length(" ",10-len(uom))
        # bill += uom


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

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]