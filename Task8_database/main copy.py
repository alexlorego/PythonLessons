import db_controller as c
from get_data import create_files as create_files
from get_data import new_base as new_base

create_files()
new_base()
c.start()
