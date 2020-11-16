import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import datetime
import os

def get_prop_sreality(location, offer, object):
    str_html = get_html_sreality(location, offer, object)
    """
    with open("sreality_html.txt", 'w', encoding="utf-8") as out_file:
         #out_file.write(soup.prettify())
         out_file.write(str_html)
    """
    soup = BeautifulSoup(str_html, "html.parser")

    all_properties = soup.find_all('div', class_='property ng-scope')

    dict_prop_sreality = {}
    list_prop_sreality = []

    for property in all_properties:
        dict_prop_sreality["int_metry"] = property.find('a', class_='title').text.strip()
        dict_prop_sreality["str_typ"] = property.find('a', class_='title').text.strip()
        dict_prop_sreality["str_address"] = property.find('span', class_='locality ng-binding').text.strip()
        dict_prop_sreality["int_cena"] = property.find('span', class_='price ng-scope').text.strip()
        dict_prop_sreality["str_url"] = "https://www.sreality.cz/" + property.find('a', class_='title')['href']
        list_prop_sreality.append(dict_prop_sreality.copy())
    return list_prop_sreality

def get_html_sreality(location, offer, object):
    #webdriver_path = r'C:\Users\NgMan\Disk Google\Freelancing\Python\Moje Projekty\webdriver\chromedriver.exe' #r obrací znaménka
    webdriver_path = os.path.dirname(os.path.realpath(__file__)) + r'\charizard\chromedriver.exe'
    print(webdriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    url = "https://www.sreality.cz/hledani/prodej/byty/praha-8,praha-7?velikost=2%2B1,3%2Bkk&cena-od=0&cena-do=6000000"
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
    driver.get(url)

    page_source = driver.page_source
    driver.quit()
    return page_source
