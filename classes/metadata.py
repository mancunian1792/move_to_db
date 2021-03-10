import tabula
import os
from itertools import chain
import re

class Metadata(object):
    def __init__(self, input_file, output_file, data_dir):
        '''
        Getting the metadata input, output and the data directories.
        @param input_file: Glossary file - Pdf where the metadata resides.
        @param output_file: .txt file with only column names suitable for writing to database.
        @param data_dir: Directory where the above files reside.
        '''
        self.input = input_file
        self.output = output_file
        self.data_dir = data_dir

    def read_metadata(self):
        '''
        If the txt file is already present just read in the text file 
        containing the column names and return as a list.
        Else, call the process metadata and read it.
        '''
        # Read the metadata columns from a text file
        if self.output in os.listdir(self.data_dir):
            # define empty list
            columns = []
            # open file and read the content in a list
            with open(self.data_dir + self.output, 'r') as f:
                filecontents = f.readlines()
                for line in filecontents:
                    # remove linebreak which is the last character of the string
                    current_place = line[:-1]
                    columns.append(current_place.strip())
            return columns
        else:
            if self.process_metadata() is not None:
                self.read_metadata()

    def write_metadata(self):
        '''
        Writing a list of columns into a file.
        '''
        # Write the metadata by reading and inferring the pdf file.
        with open(self.data_dir + self.output, 'w') as f:
            f.writelines("%s\n" % col for col in self.columns)
    
    def process_metadata(self, write_to_file=True):
        '''
        Read the glossary , a .pdf file using tabula and extract the columns as a list
        '''
        if self.input not in os.listdir(self.data_dir):
            return None
        all_pages = tabula.read_pdf(self.data_dir + self.input, pages='all')
        cols = []
        for page in all_pages:
            if "Unnamed: 0" in page.columns:
                cols.append(page["Field\rPosition"])
            else:
                cols.append(page["Field Name"])
        self.columns = list(chain(*cols))
        modify_cols = []
        regex = re.compile('[^a-zA-Z_]')
        for col in self.columns:
            col = '_'.join(col.split()).lower()
            col = regex.sub('', col)
            modify_cols.append(col)
        self.columns = modify_cols
        if write_to_file:
            self.write_metadata()

    def delete_metadata(self):
        '''
        Delete the txt metadata file.
        '''
        # Delete the created metadata file
        os.remove(self.data_dir + self.output)