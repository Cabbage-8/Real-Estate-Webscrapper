from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime
import re 


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

def get_prop_Prazskereality(location, offer, object):
    
    str_Sitename = "Prazskereality"

    # Get current date time stamp in format YYYYMMDD_HHmmSS
    str_OutputFilename = str_Sitename + '_' + GetDateTimeStamp() + '.txt'

    str_URLSearch = "https://www.prazskereality.cz/byty-na-prodej/praha/p-1"

    int_Page = 1

    while 1:

        int_Page += 1
    
        resp_PrazskerealitySearch = urllib.request.urlopen(str_URLSearch)

        soup_PrazskerealitySearch = BeautifulSoup(resp_PrazskerealitySearch, 'html.parser')

        #print(soup_PrazskerealitySearch.prettify())

        #raise SystemExit(0)

        # Prepare header for output file
        file_Output = open(str_OutputFilename, 'w')
        file_Output.write('Link' + ';' +  'Type' + ';' +  'Size' + ';' +  'Location' + ';' +  'Street' + ';' +  'Price\n')
        file_Output.close()

        # Get all offers on page
        tag_Offers = soup_PrazskerealitySearch.find_all('div', class_="results-list-item")

        dict_prop_Prazskereality = {}
        list_prop_Prazskereality = []

        for tag_Offer in tag_Offers:
            # Link
            tag_Description = tag_Offer.find_all('div', class_="text")
            #print (tag_Offer.prettify())
            #print(tag_Description.string)
            
            #print(type(tag_Offer))
            #print(type(tag_Description))


            #^.+m2.+Kč

            pattern_Description = r'^.+m2.+Kč'
            str_Description = re.findall(pattern_Description, str(tag_Offer.get_text()))

            print(str_Description)
            #print(tag_Offer.get_text())
            
            raise SystemExit(0)

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

            #print(str_Link, str_Type, str_Size, str_Location, str_Street, str_Price)

            dict_prop_Prazskereality["int_metry"] = str_Size
            dict_prop_Prazskereality["str_typ"] = str_Type
            dict_prop_Prazskereality["str_address"] = str_Location + ', ' + str_Street
            dict_prop_Prazskereality["int_cena"] = str_Price
            dict_prop_Prazskereality["str_url"] = str_Link
            list_prop_Prazskereality.append(dict_prop_Prazskereality.copy())

        tag_Pages = soup_PrazskerealitySearch.select('li > a')

        pattern_FindPage = r'\"[^\"]*\/page\/' + str(int_Page) + '\/[^\"]*\"'
        list_Pages = re.findall(pattern_FindPage, str(tag_Pages))

        if len(list_Pages) > 1:
            str_Page = list_Pages[0]
            str_Page = str_Page[1:]
            str_Page = str_Page[:-1]

            str_URLSearch = str_Page
            print("Found page " + str(int_Page) + ": " + str_Page)
        else:
            print("Page " + str(int_Page) + " not found, ending.")
            break
        
    return list_prop_Prazskereality

get_prop_Prazskereality("","","")

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

#bytes_PrazskerealitySearch = resp_PrazskerealitySearch.read()

#str_PrazskerealitySearch = bytes_PrazskerealitySearch.decode("utf8")

#resp_PrazskerealitySearch.close()

#file_MaximTextExample = open("Maxim_FirstPage.txt", "w")
#print(str_PrazskerealitySearch)
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
