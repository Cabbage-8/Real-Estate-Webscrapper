from bs4 import BeautifulSoup
import requests
import urllib.request

str_URLMaximaSearch = "https://www.maxima.cz/nabidka-nemovitosti/?advert_function=1&advert_type=1&advert_price-min=&advert_price-max=&floor_number-min=&floor_number-max=&usable_area-min=&usable_area-max=&estate_area-min=&estate_area-max="

resp_MaximaSearch = urllib.request.urlopen(str_URLMaximaSearch)

bytes_MaximaSearch = resp_MaximaSearch.read()

str_MaximaSearch= bytes_MaximaSearch.decode("utf8")

resp_MaximaSearch.close()

file_MaximTextExample = open("Maxim_FirstPage.txt", "w")
#file_MaximTextExample.write(str_MaximaSearch)
print(str_MaximaSearch)
file_MaximTextExample.close()

# Get list of all available items on current search page



##
##
##fp = urllib.request.urlopen("http://www.python.org")
##mybytes = fp.read()
##
##mystr = mybytes.decode("utf8")
##fp.close()
##
##print(mystr)
