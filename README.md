Flow Log File Parser

This project parses AWS VPC flow log data, generates tag counts based on a lookup table, and produces port/protocol counts. It's designed to process Version 2 flow logs and provide insightful statistics about network traffic.


Files
- fileParser.py: Main script that processes the flow log data and generates output files
- csvToDict.py: Utility script for converting CSV files to dictionaries
- lookupDict.py: Script that creates a lookup dictionary from lookupTable.csv
- protocolDict.py: Script that creates a protocol dictionary from protocol-numbers-1.csv
- flowLogData.txt: Sample input flow log data
- lookupTable.csv: Lookup table for port-protocol combinations and their tags

Assumptions
1. The program only supports the default log format (Version 2).
2. The flow log data file is named 'flowLogData.txt' and is in the same directory as the scripts.
3. The lookup table file is named 'lookupTable.csv' and is in the same directory as the scripts.
4. The protocol numbers CSV file is named 'protocol-numbers-1.csv' and is in the same directory as the scripts.

How to Run
1. Ensure all files are in the same directory.
2. Run the main script using Python 3 by executing the command "python fileParser.py" in the terminal.
3. The script will generate two output files:
   - tag_counts.csv: Contains the count of each tag
   - port_protocol_counts.csv: Contains the count of each port-protocol combination

Tests Performed
1. Tested with the provided sample data in flowLogData.txt
2. Verified correct parsing of different protocol numbers and their corresponding keywords
3. Checked proper handling of tagged and untagged entries
4. Ensured correct counting and output generation for both tag counts and port-protocol counts

Additional Analysis
- The program efficiently uses dictionary data structures to minimize lookup times and improve performance.
- Error handling is implemented for invalid protocol numbers in the protocol dictionary creation.
- The code is modular, with separate files for different functionalities, improving readability and maintainability.
- Comments are included throughout the code to explain the logic and improve understanding.
