import csv

# Read the CSV file
with open('deathrow.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Get the column you want to extract
    column_to_extract = [row[8] for row in reader]

    # Create a new text file
    with open('deathrow_statement.txt', 'w') as textfile:
        for item in column_to_extract:
            if item != "decline":
                textfile.write(item + '\n\n')

# Close the files
csvfile.close()
textfile.close()