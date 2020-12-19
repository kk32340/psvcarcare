from db import *
from num2words import num2words 

def getdocument(details):
    bill="""
    <!DOCTYPE html>
    <html lang="en">
    <head>        
    </head>
    <body>
        <table width="100%">       
        <tr> 
            <th width="70%" align="left">PSP CAR CARE</th>
            <th width="30%" rowspan="3" align="left">
                <img src="./image/logo.jpg"/>
            </th>
        </tr> 
        <tr> 
            <th width="70%" colspan="2" align="left">1223/6B, BY-PASS ROAD</th>
        </tr>  
        <tr> 
            <th width="70%" colspan="2" align="left">SHANMUGANATHI, PALANI-624 602</th>
        </tr> 
        <tr> 
            <th width="70%"  align="left">EMAIL:pspcarcare@gmail.com</th>
            <th width="30%"  align="left">{details.invoiceno}</th>
        </tr>
        <tr> 
            <th width="70%"  align="left">PHONE NO: 9944429143, 9787703040</th>
            <th width="30%"  align="left">{details.date_modified}</th>
        </tr>
        <tr>
            <th colspan='2' width='100%' style="border-bottom-style: solid;border-width: 1px;">  
                           
            </th>
        </tr>
        <tr style="border-color:black" border-color="black">
            <th align="center" colspan="2">
                <h3>RETAIL CASH BILL</h3>
            </th>
        </tr>
        <tr> 
            <th width="70%"  align="left">{details.custname}</th>
            <th width="30%"  align="left">{details.vehicleno}</th>
        </tr>
        <tr> 
            <th width="70%"  align="left">{details.custadd}</th>
            <th width="30%"  align="left">{details.vehicleinfo}</th>
        </tr>
        <tr> 
            <th width="70%"  align="left">{details.mobileno}</th>
            <th width="30%"  align="left">{details.kilometer}</th>
        </tr>
    </table>
    """    

    bill = bill.replace("{details.invoiceno}","INVOICE NO:" + details.invoiceno)
    bill = bill.replace("{details.date_modified}","INVOICEDATE:" + details.date_modified.strftime("%d/%m/%Y")) if details.date_modified !=None else ""
    bill = bill.replace("{details.custname}","CUSTOMER NAME: "+details.custname)
    bill = bill.replace("{details.vehicleno}","VEHICLE REG. No:" + details.vehicleno)
    bill = bill.replace("{details.custadd}","ADDRESS: "+details.custadd)
    bill = bill.replace("{details.vehicleinfo}","MAKE / MODEL:" + details.vehicleinfo)
    bill = bill.replace("{details.mobileno}","PHONE NO.: "+details.mobileno)
    bill = bill.replace("{details.kilometer}","KILO METER:" + details.kilometer if details.kilometer !=None else "")


    bill2="""
    <table  
           width="100%"> 
        <tr>
            <th colspan='17' width='100%' style="border-bottom-style: solid;border-width: 1px;"> 
            </th>
        </tr>
        <tr> 
            <th colspan='1' align="left">S.No</th> 
            <th colspan='8'  align="left">ITEM DESCRIPTION</th> 
            <th colspan='2'  align="right">QUANTITY</th>
            <th colspan='2'  align="right">UNIT</th>
            <th colspan='2'  align="right">AMOUNT</th> 
            <th  colspan='2' align="right">TOTAL</th> 
        </tr> 
        <tr>
            <th colspan='17' width='100%' style="border-bottom-style: solid;border-width: 1px;">
            </th>
        </tr>
    """

    gtotal=0
    material_item_index=0
    htmlstr=""
    for i in details.items:
        if i.itemtype=="Material":
            material_item_index +=1
            gtotal += i.total
            htmlstr += "<tr>"
            htmlstr += "<th colspan='1' align='left' >" + str(material_item_index) + "</th>" 
            htmlstr += "<th colspan='8' align='left' >" + i.itemname.upper() + "</th>"  
            htmlstr += "<th colspan='2' align='right' >" + str(i.qty) + "</th>" 
            htmlstr += "<th colspan='2' align='right' >" + i.uom.upper() + "</th>"            
            htmlstr += "<th colspan='2' align='right' >" + str(i.price) + "</th>" 
            htmlstr += "<th colspan='2' align='right' >" + str(i.total) + "</th>"          
            htmlstr += "</tr>"
    
    gtotal=float("{:.2f}".format(gtotal))

    #htmlstr +="<tr><th colspan='15'></th><th  align='right' colspan='2' style='border-bottom-style: solid;border-width: 1px;'></th></tr>"

    #htmlstr +="<tr><th colspan='10'></th><th  align='right' colspan='7' ><h3>"+ "Total:" + str(gtotal) +"</h3></th></tr>"

    service_item_index=0
    for i in details.items:
        if i.itemtype=="Labour":
            service_item_index +=1
            if service_item_index==1:                
                htmlstr +="<tr><th width='10' align='center' colspan='17'>" + "<h3>LABOUR CHARGES:</h3>" +"</th></tr>"
            gtotal += i.total

            htmlstr += "<tr>"
            htmlstr += "<th align='left' colspan='1'>" + str(service_item_index) + "</th>" 
            htmlstr += "<th align='left' colspan='14' width='85%'>" + i.itemname.upper() + "</th>"
            htmlstr += "<th align='right' colspan='2'>" + str(i.total) + "</th>"          
            htmlstr += "</tr>"

    htmlstr +="""
        <tr >
            <th colspan='17' width='100%' style="border-bottom-style: solid;border-width: 1px;"> 
            </th>
        </tr>
    """
    gtotal=float("{:.2f}".format(gtotal))

    htmlstr +="<tr><th colspan='10'>"+ num2words(gtotal, lang ='en') +"</th><th align='right' colspan='7'><h3>"+ "Total:" + str(gtotal) +"</h3></th></tr>"

    htmlstr +="""
        <tr>
            <th colspan='17' width='100%' style="border-bottom-style: solid;border-width: 1px;">                             
            </th>
        </tr>
    """
    htmlstr +="""
        <tr>
            <th colspan='17'>
            </br>                  
            </th>
        </tr>
     """

    htmlstr +="<tr><th width='100%' align='right' colspan='17'>"+ "For PSP CAR CARE" +"</th></tr>"

    returnstr=bill + bill2 + htmlstr + "</table>"

    returnstr +="</body></html>"

    # f = open("test1.html", "a")
    # f.write(returnstr)
    # f.close()

    return returnstr

def getdocument1(details):
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