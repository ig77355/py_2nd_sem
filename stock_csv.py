from csv import DictWriter, DictReader
from pathlib import Path


def process_csv_file(csv_file_in):
    directory = Path(csv_file_in.parent)
    # defining new file name
    csv_file_out = directory.joinpath(csv_file_in.stem + "_new" + csv_file_in.suffix)
    with open(csv_file_in, 'r') as f_in:
        reader = DictReader(f_in, delimiter=',')
        # checking if the file contains stock data
        if 'Open' in reader.fieldnames and 'Close' in reader.fieldnames:
            fieldnames_out = reader.fieldnames
            fieldnames_out.append('Change')
            # writing the file
            with open(csv_file_out, 'w', newline='') as f_out:
                writer = DictWriter(f_out, fieldnames=fieldnames_out)
                writer.writeheader()
                for row in reader:
                    # calculating change
                    change = ((float(row['Close'])) - (float(row['Open']))) / (float(row['Open']))
                    # adding change to the dictionary
                    row['Change'] = str(change)
                    writer.writerow(row)


# my local path to the csv files
path = Path('I:\$Download\pypy')
for file in path.iterdir():
    # making sure that we take csv files only
    if file.is_file() and file.match('*.csv'):
        process_csv_file(file)