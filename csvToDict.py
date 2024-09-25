import csv

def csv_to_dict(file_path, key_column, value_column=None):
    # Create an empty dictionary to store our results
    result = {}

    # Open the specified CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Loop through each row in the CSV file
        for row in reader:
            # Use the specified column as the key, removing any leading/trailing whitespace
            key = row[key_column].strip()

            # If a specific value column is provided, use it as the value
            if value_column:
                value = row[value_column].strip()
            else:
                # Otherwise, create a dictionary of all other columns
                value = {}

                for column, data in row.items():
                    # Skip the key column and remove whitespace from both column names and data
                    if column != key_column:
                        value[column.strip()] = data.strip()

            # Add the key-value pair to our result dictionary
            result[key] = value

    # Return the completed dictionary
    return result