import sys 
import gumbo

input_path = sys.argv[1]
output_path = sys.argv[2]

# call the HTML parser object
x = gumbo.parseHTML()

# parse the HTML from path to table 
table = x.parse_path(input_path)

# table to list
list = x.parse_html_table(table) 

# list to CSV
x.html_to_csv(list, output_path)  

