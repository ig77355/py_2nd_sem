import os
import csv
stock_file =

if os.path.exists(stock_file):
    with open(stock_file, 'rw', ) as f:
        reader = csv.DictReader(f, delimiter=',') #csv.reader?
        for row in reader:

        writer = csv.DictWriter(f, delimeter = ',')  #csv writer?
        for row in writer
# next(csv_reader) # skip the heading, code after reader = csv.DictReader(f)
# https://thepythonguru.com/python-how-to-read-and-write-csv-files/
