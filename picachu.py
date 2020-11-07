from sreality import *

def get_properties(location, offer, object):
    list_prop = []

    list_prop.extend( get_prop_sreality(location, offer, object) )
    #list_prop.extend( get_prop_maxima(location, offer, object) )
    return list_prop


def add_new_properties_to_db(database, list_property):
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
