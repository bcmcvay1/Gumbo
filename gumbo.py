import csv
import pandas as pd
from bs4 import BeautifulSoup

class parseHTML: 

    def parse_path(self, in_path): 
        file = open(in_path, 'rb')
        soup = BeautifulSoup(file, 'lxml') 
        table = soup.find_all("table") 
        return table 
        
    def parse_html_table(self, table): 
        table = table[1] 
        output_rows = []
        header_row = [] 
        
        for table_header in table.findAll('th'): 
            header_row.append(table_header.text) 

        output_rows.append(header_row) 
        
        for table_row in table.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                new_line = (column.text).replace('\n','[newline]')
                output_row.append(new_line)
            output_rows.append(output_row)
  
        return output_rows
        
    def html_to_csv(self, list, out_path): 
        with open(out_path, 'w', encoding = 'utf-8-sig', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',', quoting = csv.QUOTE_ALL)
            writer.writerows(list)