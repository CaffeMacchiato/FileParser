from csvToDict import csv_to_dict

# Read the CSV file into a dictionary
raw_lookup_table = csv_to_dict('lookupTable.csv', 'dstport')

# Create the final lookup dictionary
lookup_dict = {}
for port, values in raw_lookup_table.items():
    protocol = values['protocol'].lower()
    tag = values['tag']

    # Create a key by combining port and protocol with a comma
    key = str(port) + "," + protocol
    lookup_dict[key] = tag
