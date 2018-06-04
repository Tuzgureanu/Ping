#!/usr/bin/env python

import os
cwd = os.getcwd()

import sys
sys.path.append(cwd)

from graphic import create_graphic
from utils import get_sql_db_table

db = 'res_db.sqlite'
#tb = ['vodafone_ro','gsp_ro']

tb = get_sql_db_table(db)

for t in tb:
    for mod in [None,'average']:
        create_graphic(db = db, tb = t, jitter = True, reach = True, mode = mod)
