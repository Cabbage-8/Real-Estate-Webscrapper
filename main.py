from picachu import *
import datetime

import_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

new_data = get_properties("x","x","x") #master task Matouš i Tuan každý 2 weby
#new_data_wo_duplicates = remove_duplicates(new_data) #task 1 Tuan
add_new_prop_to_db("database.csv", new_data_wo_duplicates)


"""todo"""
#postavit webovou aplikaci
#nástroje
#docker #jenkins
#linux
#databáze
#javascript, css, html
