'''
This calls a configuration file for the parameters necessary for database access. Note it calls MY copy of credentials.csv; I did not upload that file to Github. Fill in the empty_credentials.csv I've included in the package main folder, and edit line 8 to point to that file!
'''
print('Imported settings...')

# Adding file to PATH - note os.getcwd() returns the characterizationPaperPackage path!
# [Add the Python subdirectory]
import os
import sys
PATH = 'D:\\Git\\characterizationPaperPackage\\inst\\py'
# curr_path = os.getcwd() + '\\inst\\py\\'
sys.path.append(PATH)

# Change the os.chdir [working directory] so that relative paths work.
os.chdir(PATH)
print('Current path: ', PATH)

# Parameters
import pandas as pd
credentials = pd.read_csv('D:\\Git\\characterizationPaperPackage\\empty_credentials.csv')
server = credentials.server.values[0] # e.g. ohda-prod-1.cldcoxyrkflo.us-east-1.redshift.amazonaws.com
db = credentials.db.values[0] # e.g. truven-ccae
user = credentials.user.values[0]
password = credentials.password.values[0]
port = credentials.port.values[0] # e.g. 5439

# Change the 'results' string to wherever the table was saved
sexdiff_cohort_ttonset_v5_tablepath = 'scratch_jhardi10' + '.sexdiff_cohort_ttonset_v5'
sex_diff_summary_tablepath = 'scratch_jhardi10' + '.sex_diff_summary'

# print(server, db, user, password)
