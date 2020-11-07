

def get_properties(min_price, max_price, location, type):
    list_property = []
    dict_property = {
        "str_address": ""
        "int_metry": 1
        "int_cena": 1
        "str_url": ""
        "str_typ": ""
    }
    get_properties_sreality(properties, min_price, max_price, location, type)
    get_properties_maxima(properties, min_price, max_price, location, type)
    return list_property


def add_new_properties_to_db(database, new_data):
