from sreality import *
import pandas as pd

def get_properties(location, offer, object):
    list_prop = []

    list_prop.extend( get_prop_sreality(location, offer, object) )
    #list_prop.extend( get_prop_maxima(location, offer, object) )
    return list_prop


def add_new_prop_to_db(database, list_property):
    open( database, 'w').close()

    dict_prop = {
        "str_address": "",
        "int_metry": 40,
        "int_cena": 100,
        "str_url": "www.hello.matous",
        "str_typ": "2+1"
    }
    with open( database, 'a', encoding="utf-8") as f:
        w = csv.DictWriter(f, dict_prop.keys())
        w.writeheader()
        w.writerows(list_property)

def filter_top_properties(database):
    df_prop = pd.read_csv(database) #index_col = 0
    df_prop["COUNTRY"] = df_prop["str_address"].apply(str.upper)
    df_prop.to_csv("tuan_test.csv", index = False, header=True)
