from picachu import *

location = ["Praha 8", "Praha 7"]
object = "Byt"
offer = "Prodej"

new_data = get_properties(location, offer, object)
add_new_properties_to_db(database, new_data)

#notifikace()
