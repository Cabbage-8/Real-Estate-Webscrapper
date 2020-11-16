from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime 


def WriteLineToOutput(str_Link, str_Type, str_Size, str_Location, str_Street, str_Price, str_OutputFilename):
    file_Output = open(str_OutputFilename, 'a')
    file_Output.write(str_Link + ';' +  str_Type + ';' +  str_Size + ';' +  str_Location + ';' +  str_Street + ';' +  str_Price + '\n')
    file_Output.close()

def GetDateTimeStamp():
    dateTimeObj = datetime.now()
    date_RunDate = str(dateTimeObj.year) + (str("0" + str(dateTimeObj.month))[-2:]) + (str("0" + str(dateTimeObj.day))[-2:])
    date_RunTime = (str("0" + str(dateTimeObj.hour))[-2:]) + (str("0" + str(dateTimeObj.minute))[-2:]) + (str("0" + str(dateTimeObj.second))[-2:])
    date_RunDatetime = str(date_RunDate) + '_' + str(date_RunTime)
    return str(date_RunDatetime)

def get_prop_maxima(location, offer, object):
    
    str_Sitename = "Maxima"

    # Get current date time stamp in format YYYYMMDD_HHmmSS


    str_OutputFilename = str_Sitename + '_' + GetDateTimeStamp() + '.txt'

    str_URLMaximaSearch = "https://www.maxima.cz/nabidka-nemovitosti/?advert_function=1&advert_type=1&advert_price-min=&advert_price-max=&floor_number-min=&floor_number-max=&usable_area-min=&usable_area-max=&estate_area-min=&estate_area-max="

    resp_MaximaSearch = urllib.request.urlopen(str_URLMaximaSearch)

    soup_MaximaSearch = BeautifulSoup(resp_MaximaSearch, 'html.parser')

    # Prepare header for output file
    file_Output = open(str_OutputFilename, 'w')
    file_Output.write('Link' + ';' +  'Type' + ';' +  'Size' + ';' +  'Location' + ';' +  'Street' + ';' +  'Price\n')
    file_Output.close()

    # Get all offers on page
    tag_Offers = soup_MaximaSearch.find_all('a', class_="details-wrapper")

    dict_prop_maxima = {}
    list_prop_maxima = []

    for tag_Offer in tag_Offers:
        # Link
        str_Link = tag_Offer.get('href')
        #print (tag_Offer.get('href'))

        # Type
        tag_Type = tag_Offer.find('span', class_="title")
        str_Type = tag_Type.string
        #print (tag_Type.string)

        # Size
        tag_Table = tag_Offer.find('table')
        tag_Rows = tag_Table.find_all('td')


        int_Iter = 0
        str_Size = ''
        str_Location = ''
        str_Street = ''
        str_Price = ''
        
        for tag_Row in tag_Rows:
            if int_Iter == 1: str_Size = tag_Row.getText()
            if int_Iter == 3: str_Location = tag_Row.getText()
            if int_Iter == 5: str_Street = tag_Row.getText()
            if int_Iter == 7: str_Price = tag_Row.getText()
            int_Iter += 1

        #WriteLineToOutput(str_Link, str_Type, str_Size, str_Location, str_Street, str_Price, str_OutputFilename)

        dict_prop_maxima["int_metry"] = str_Size
        dict_prop_maxima["str_typ"] = str_Type
        dict_prop_maxima["str_address"] = str_Location + ', ' + str_Street
        dict_prop_maxima["int_cena"] = str_Price
        dict_prop_maxima["str_url"] = str_Link
        list_prop_maxima.append(dict_prop_maxima.copy())
        
    return list_prop_maxima

    #break

 #raise SystemExit(0)
  #  ('h1' + ';' +  class_="title")
#    hrefs = tag_Table.find_all('a', class="details-wrapper")

 #   print(len(hrefs))
    #for href in hrefs:
    #    print (href.get('href'))

    #print(div)
#print(len(list_Tables))

#print(*list_Tables, sep='\n')

#________________________________________________
# Save html as txt file

#bytes_MaximaSearch = resp_MaximaSearch.read()

#str_MaximaSearch = bytes_MaximaSearch.decode("utf8")

#resp_MaximaSearch.close()

#file_MaximTextExample = open("Maxim_FirstPage.txt", "w")
#print(str_MaximaSearch)
#file_MaximTextExample.close()
#________________________________________________




##
##
##fp = urllib.request.urlopen("http://www.python.org")
##mybytes = fp.read()
##
##mystr = mybytes.decode("utf8")
##fp.close()
##
##print(mystr)
