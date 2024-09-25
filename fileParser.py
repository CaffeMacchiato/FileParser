import csv
from csvToDict import csv_to_dict
from protocolDict import protocol_dict
from lookupDict import lookup_dict



# This is the function to read from 'flowLogData.txt'
def parse_flow_log(line):
    # First, split the line into fields
    fields = line.strip().split()

    # Then, extract dstport (7th field, index 6)
    dstport = int(fields[6])

    # Then, extract protocol (8th field, index 7)
    protocol = int(fields[7])

    # Finally, convert protocol number to keyword
    protocol_keyword = protocol_dict.get(protocol, "unknown_protocol")

    # And then return these values
    return dstport, protocol_keyword



# This function looks up the tag for a given 'dstport' and 'protocol' within the 'lookup_table' dictionary (in main())
def get_tag_from_lookup(dstport, protocol, lookup_table):
    # Create a key by combining dstport and protocol with a comma
    key = str(dstport) + "," + protocol.lower()

    # If the key exists in the lookup table,
    if key in lookup_table:
        return lookup_table[key]  # return this key's value
    else:  # Otherwise,
        return "Untagged"  # return a fallback value



def main():
    # First, initialize dictionaries to store our counts
    tag_counts = {}
    port_protocol_counts = {}

    # Since the .csv files are already being processing elsewhere, the program now uses 'lookup_dict'

    # This processes the flow log data
    with open('flowLogData.txt', 'r') as flow_log_file:
        for line in flow_log_file:
            # Parse each line of the flow log
            dstport, protocol_keyword = parse_flow_log(line)

            # Get the tag for this combination
            tag = get_tag_from_lookup(dstport, protocol_keyword, lookup_dict)

            # Update the tag counts
            # If this tag has been seen before, then add 1 to its count
            # If it's new, then start its count at 1
            if tag in tag_counts:
                tag_counts[tag] += 1
            else:
                tag_counts[tag] = 1


            # Update the port/protocol combination counts
            # Make a key by combining the port and protocol
            port_protocol_key = str(dstport) + "," + protocol_keyword


            # Same thing as with tags count
            # If it's been seen, add 1
            # If not, start at 1
            if port_protocol_key in port_protocol_counts:
                port_protocol_counts[port_protocol_key] += 1
            else:
                port_protocol_counts[port_protocol_key] = 1



    # Now write the results to .csv files
    # First, create and write to the tag counts file, 'tag_counts.csv'
    with open('tag_counts.csv', 'w', newline='') as tag_file:
        writer = csv.writer(tag_file)  # .writer() is a .csv file-specific method
        writer.writerow(['Tag', 'Count'])  # This is the header row

        # Now write each tag and its count
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])


    # Now write the port/protocol counts
    with open('port_protocol_counts.csv', 'w', newline='') as port_protocol_file:
        writer = csv.writer(port_protocol_file)  # .writer() is a .csv file-specific method
        writer.writerow(['Port', 'Protocol', 'Count'])  # This is the header row again

        # Write each port/protocol combination and its count
        for port_protocol_key, count in port_protocol_counts.items():
            port, protocol = port_protocol_key.split(',')  # Split up the output with a comma
            writer.writerow([port, protocol, count])

    print("Processing complete. Check tag_counts.csv and port_protocol_counts.csv for results.")


if __name__ == "__main__":
    main()
