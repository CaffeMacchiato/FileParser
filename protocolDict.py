# This program makes a dictionary out of the .csv file 'protocol-numbers-1.csv'.

# I've used the table at the link: https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
# Since there are a lot of protocols in the table provided in the link above,
# my implementation of the dictionary reads from the .csv file 'protocol-numbers-1.csv'
# and generates the dictionary below.


from csvToDict import csv_to_dict

# Read the CSV file into a dictionary
raw_protocol_dictionary = csv_to_dict('protocol-numbers-1.csv', 'Decimal', 'Keyword')

# Convert keys to integers and values to lowercase
protocol_dict = {}
for key, value in raw_protocol_dictionary.items():
    lowercase_value = value.lower()

    # This code handles range values
    if '-' in key:
        start, end = map(int, key.split('-'))
        for i in range(start, end + 1):
            protocol_dict[i] = lowercase_value
    else:
        try:
            int_key = int(key)
            protocol_dict[int_key] = lowercase_value
        except ValueError:
            print(f"Warning: Skipping invalid key '{key}' in protocol-numbers-1.csv")

print(f"Loaded {len(protocol_dict)} protocol entries.")
