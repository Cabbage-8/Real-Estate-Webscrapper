from picachu import *
import datetime

location = ["Praha 8", "Praha 7"]
object = "Byt"
offer = "Prodej"


import_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

new_data = get_properties(location, offer, object)
add_new_prop_to_db("database.csv", new_data)
#filter_top_properties("database.csv")
#notifikace()
