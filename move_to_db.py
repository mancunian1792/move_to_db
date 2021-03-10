import pandas as pd
from pandas.io import sql
import subprocess
import os
from datetime import datetime
from tqdm import tqdm
from classes.metadata import Metadata
from classes.connection import Connection
from sqlalchemy import event
import gc
import argparse
import logging
import time

logging.basicConfig(filename='avenue_gp.log', level=logging.DEBUG)
CHUNKSIZE = 100000

def process_csv_file(file_name, columns, engine, table_name, chunksize=100000):
    '''
    Process each csv by chunk and move them to a relational database.
    @param file_name: Name of the CSV file to be read.
    @param columns: list of column names of the csv.
    @param engine: MySQL connection engine through SQLALCHEMY
    @param table_name: Table Name where the data needs to be pushed.
    @param chunksize: Number of records to be read and processed at one go.
    @returns None
    '''
    try:
        logging.debug(f"Currently processing {file_name}")
        # Get number of lines in the CSV file
        num_lines = subprocess.check_output('wc -l %s' % file_name, shell=True)
        num_lines = int(num_lines.split()[0]) 
        # Iteratively read CSV and dump lines into the mysql table
        for i in tqdm(range(0, num_lines, chunksize)):
            logging.debug(f"Currently processing chunk {i} of {num_lines} of file {file_name}")
            df = pd.read_csv(file_name,  
                    header=None,  # no header, define column header manually later
                    nrows=chunksize, # number of rows to read at each iteration
                    skiprows=i,# skip rows that were already read
                    sep='|',
                    low_memory=False)
            assert df.shape[1] == len(columns)   

            # columns to read        
            df.columns = columns
            df["created_by"] = "pipeline"
            df["created_at"] = datetime.now()
            '''
            
            The below works but my machine gets stuck everytime.
            This could be faster than the current method.
            sql.to_sql(df, 
                        name=table_name, 
                        con=engine, 
                        index=False, # don't use CSV file index
                        if_exists='append',
                        method='multi') 
            '''
            df.to_sql(  name=table_name, 
                        con=engine, 
                        index=False, # don't use CSV file index
                        if_exists='append') 
            del df
            gc.collect()
        logging.debug(f"Finished processing the file. {file_name}")
    except Exception as e:
        logging.info("----------------------------------------------------------------")
        logging.exception(f"Error occured.Check logs {e}")
        logging.info("----------------------------------------------------------------")
    

def get_all_files(data_dir):
    '''
    Get all the required files to be processed.
    @param data_dir: The directory where the files are to be processed.
    @returns csv_files: List<str> A list of csv files to be processed
    '''
    files = os.listdir(data_dir)
    csv_files = [f for f in files if f.endswith('.csv')]
    return csv_files
    '''
    print("last modified: %s" % time.ctime(os.path.getmtime(data_dir + file)))
    Can do something with last modified date and check for files that are updated only in
    this quarter. 
    '''


if __name__ == '__main__':
    
    # Parse the command line arguments.
    parser = argparse.ArgumentParser(description="parse args")
    parser.add_argument('-data_dir', '--dir', default="./data/", type=str, help='The input data directory')
    args = parser.parse_args()

    # columns that should be read from the CSV file
    metadata = Metadata(input_file='glossary.pdf', output_file='columns.txt', data_dir=args.dir)
    columns = metadata.read_metadata()

    # connect to database
    con = Connection()
    engine = con.connect_to_database(return_as_string=False)
    table_name = os.getenv("tablename")

    @event.listens_for(engine, 'before_cursor_execute')
    def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
        if executemany:
            cursor.fast_executemany = True

    # Get all the files that needs to be moved to DB
    csv_files = get_all_files(args.dir)

    # Process each file. -> This could be parallelized using multiprocessing module.
    for file in tqdm(csv_files):
        process_csv_file(args.dir+file, columns, engine, table_name, CHUNKSIZE)
    
    engine.dispose()
