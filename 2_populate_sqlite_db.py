# %%
import sqlite3
import pandas as pd
import glob

from os import listdir
from os.path import isfile, join

# %%
# Pull all data files to onboard to dB
data_folder_path = r'results/*' # all files in {results}

# %%
# load in all files 
loaded_files = [pd.read_csv(filename) for filename in glob.glob(data_folder_path)]

# %%
# load in all file names & clean the tail ".csv" off each value
loaded_files_names = [f for f in listdir(data_folder_path[:-1]) if isfile(join(data_folder_path[:-1], f))] 
loaded_files_names_rcsv = [str.rstrip(".csv") for str in loaded_files_names]

assert len(loaded_files) == len(loaded_files_names) # check if num of files == num of file names

# %%
# Connect to the database
database_path = 'DAP_database.db'
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# %%
# Write data files to database
for file_name, file in zip(loaded_files_names_rcsv, loaded_files):

    table_name = file_name
    file.to_sql(table_name, 
                conn, 
                if_exists= 'replace') ## Maybe check content before replacing a file

# %%
conn.close()


