from db import *
from num2words import num2words 

def getdocument(details):
    bill=""
    bill += "PSP"
    bill += "\n" + "CAR CARE"
    bill += "\n" + "1223/6B, BY-PASS ROAD"
    bill += "\n" + "SHANMUGANATHI, PALANI-624 602"    

    bill += "\n" + "{:\u2000<61s}".format("EMAIL:pspcarcare@gmail.com")
    bill += "{:\u2000<20s}".format("INVOICE NO:" + details.invoiceno)

    bill += "\n" + "{:\u2000<60s}".format("PHONE NO: 9944429143, 9787703040")
    bill += "{:\u2000<20s}".format("INVOICEDATE:" + details.date_modified.strftime("%m/%d/%Y %H:%M"))
    
    bill += "\n"
    bill += "{0:->94}".format("")
    bill += "\n"
    bill += "{:\u2000^94s}".format("RETAIL CASH BILL")
    
    bill += "\n" + "{:\u2000<61s}".format("CUSTOMER NAME: "+details.custname)
    bill += "{:\u2000<20s}".format("VEHICLE REG. No:" + details.vehicleno)
    
    bill += "\n" + "{:\u2000<61s}".format("ADDRESS: "+details.custadd)
    bill += "{:\u2000<20s}".format("MAKE / MODEL:" + details.vehicleinfo)
    
    bill += "\n" + "{:\u2000<61s}".format("PHONE NO.: "+details.mobileno)
    bill += "{:\u2000<20s}".format("KILO METER:" + details.kilometer)
    bill += "\n"
    
    bill += "{0:->94}".format("")
    bill += "\n"
    
    bill += "{:\u2000^6s}".format("S.No")
    bill += "{:\u2000<60s}".format("ITEM DESCRIPTION") 
    bill += "{:\u2000>6s}".format("UNIT") 
    bill += "{:\u2000>10s}".format("QUANTITY") 
    bill += "{:\u2000>10s}".format("AMOUNT") 
    bill += "{:\u2000>10s}".format("TOTAL") 
    bill += "\n"
        
    bill += "{0:->94}".format("")
    bill += "\n"
    gtotal=0
    material_item_index=0
    for i in details.items:
        if i.itemtype=="Material":
            material_item_index +=1
            gtotal += i.total
            bill += "{:\u2000^6s}".format(str(material_item_index))

            bill += "{:\u2000<60s}".format(i.itemname.upper()[0:50])
            bill += "{:\u2000^6s}".format(i.uom.upper())

            bill += "{:\u2000>10s}".format(str(i.qty)) 
            bill += "{:\u2000>10s}".format(str(i.price)) 
            bill += "{:\u2000>10s}".format(str(i.total)) 
            bill += "\n"

    bill += "{0:->94}".format("")
    bill += "\n"
    bill += "{0:>74}".format("Total:")
    bill += "{0:>15}".format(str(gtotal))
    bill += "\n"
    #bill += "{0:->94}".format("")

    service_item_index=0
    for i in details.items:
        if i.itemtype=="Labour":
            service_item_index +=1
            if service_item_index==1:
                bill += "\n"
                bill += "{0:>40}".format("Labour charges:")
                bill += "\n"
                bill += "\n"
            gtotal += i.total
            #bill += "{:\u2000^6s}".format(str(i.slno))
            bill += "{:\u2000<92s}".format(i.itemname.upper()[0:80])
            # bill += "{:\u2000^6s}".format(i.uom.upper())
            # bill += "{:\u2000>10s}".format(str(i.qty)) 
            # bill += "{:\u2000>10s}".format(str(i.price)) 
            bill += "{:\u2000>10s}".format(str(i.total)) 
            bill += "\n"

    bill += "{0:->94}".format("")
    bill += "\n"
    bill += "{0:<60}".format(num2words(gtotal, lang ='en'))
    bill += "{0:>14}".format("Total:")
    bill += "{0:>15}".format(str(gtotal))
    bill += "\n"
    bill += "{0:->94}".format("")
    bill += "\n"
    bill += "\n"
    bill += "{0:>90}".format("For PSP CAR CARE")

    #num2words(36, lang ='es')
    return bill

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]