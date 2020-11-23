import os
from picachu import *
import datetime


xxx = get_prop_sreality("x","x","x")
print(len(xxx))
add_new_prop_to_db("temp_test.csv", xxx)
