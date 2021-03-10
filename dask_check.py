import sqlalchemy as sa
import dask.dataframe as dd
from dask.diagnostics import ProgressBar
from classes.metadata import Metadata
from classes.connection import Connection
from datetime import datetime

#ddf = dd.read_csv('./data/2019Q3.csv')
metadata = Metadata(input_file='glossary.pdf', output_file='columns.txt', data_dir='./')
columns = metadata.read_metadata()
ddf = dd.read_csv('./data/2020Q2.csv', header=None, sep='|', names = columns, assume_missing=True, low_memory=False)
con = Connection()
engine = con.connect_to_database(return_as_string=True)
start_time = datetime.now()
ddf.to_sql('Loan_Performance_Batch', uri=engine, if_exists='append', index=False, parallel=True)
end_time = datetime.now()
print(f"It took {((end_time - start_time).seconds)/60} minutes")
#server = 'localhost:3306'
#pbar = ProgressBar()
#pbar.register()
#windows authentication + fast_executemany=True
#to_sql_uri = sa.create_engine(f'mssql://@{server}/{database}?trusted_connection=yes&driver={driver_name}', fast_executemany=True)
#ddf.to_sql('PowerBI_Report', uri=to_sql_uri, if_exists='replace', index=False)