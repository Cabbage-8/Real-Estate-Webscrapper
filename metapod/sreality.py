import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import datetime
import os
import re

def extract_type(my_string):
    my_pattern = r'(\d+\d|\d+kk|6 pokojů a více|atypické)' #hledání 4 typů na sreality
    return re.findall(my_pattern, str(my_string))[0]

def extract_meters(my_string):
    my_pattern = r'\d+ m²'
    return re.findall(my_pattern, str(my_string))[0][:-3]

#"[^"]strana=\d+[^"]"

def get_list_of_pages(my_soup):
    list_of_pages = my_soup.find("ul", class_="paging-full")
    list_of_links = []
    if list_of_pages is not None:
        for x in list_of_pages.find_all("li", class_="paging-item ng-scope"):
            my_link = "https://www.sreality.cz/" + x.find('a')['href']
            list_of_links.append(my_link)
            print(f"getting list of pages {my_link}")#tohleeeeee pak vymaaaaaz
    return list_of_links

def extract_props_from_html(my_soup):
    all_properties = my_soup.find_all('div', class_='property ng-scope')
    dict_prop_sreality = {}
    list_prop_sreality = []
    with open("my_output.txt", 'a', encoding="utf-8") as out_file:

        for property in all_properties:
            dict_prop_sreality["int_metry"] = property.find('a', class_='title').text.strip()
            dict_prop_sreality["str_typ"] = property.find('a', class_='title').text.strip()
            dict_prop_sreality["str_address"] = property.find('span', class_='locality ng-binding').text.strip()
            dict_prop_sreality["int_cena"] = property.find('span', class_='price ng-scope').text.strip()
            dict_prop_sreality["str_url"] = "https://www.sreality.cz/" + property.find('a', class_='title')['href']
            list_prop_sreality.append(dict_prop_sreality.copy())
    return list_prop_sreality

def get_prop_sreality(location, offer, object):
    url = "https://www.sreality.cz/hledani/prodej/byty/praha-8,praha-7?velikost=2%2B1,3%2Bkk&cena-od=0&cena-do=6000000"
    str_html = get_html_sreality(url)

    with open("delete_this.txt", 'w', encoding="utf-8") as out_file:
         #out_file.write(soup.prettify())
         out_file.write(str_html)

    soup = BeautifulSoup(str_html, "html.parser")
    pages = get_list_of_pages(soup)

    list_prop_sreality = []
    list_prop_sreality.extend(extract_props_from_html(soup))

    for page in pages[1:]:
        print(f"this is the page we are scraping now {page}")
        str_html_2 = get_html_sreality(page)
        soup = BeautifulSoup(str_html_2, "html.parser")
        list_prop_sreality.extend(extract_props_from_html(soup))
    return list_prop_sreality

def get_html_sreality(url):
    #webdriver_path = r'C:\Users\NgMan\Disk Google\Freelancing\Python\Moje Projekty\webdriver\chromedriver.exe' #r obrací znaménka
    webdriver_path = os.path.dirname(os.path.realpath(__file__)) + r'\charizard\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
    driver.get(url)

    page_source = driver.page_source
    driver.quit()
    return page_source
