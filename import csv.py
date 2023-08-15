import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Read CSV and convert to XML
def csv_to_rss(csv_file, xml_file):
    root = ET.Element('rss')
    root.set('version', '2.0')
    
    channel = ET.SubElement(root, 'channel')
    ET.SubElement(channel, 'title').text = 'KD DIP'
    ET.SubElement(channel, 'link').text = 'https://drive.google.com/drive/folders/1Lk5NkKp5cnFpUqtxxtvUO9BQ2LHovB-J'
    ET.SubElement(channel, 'description').text = 'DIP Podcasts'

    with open(csv_file, 'r') as csv_input:
        csv_reader = csv.reader(csv_input)
       # next(csv_reader)  # Skip header row

        for row in csv_reader:
            item = ET.SubElement(channel, 'item')
            ET.SubElement(item, 'title').text = row[0]
            ET.SubElement(item, 'link').text = row[1]
            ET.SubElement(item, 'description').text = row[2]
            ET.SubElement(item, 'pubDate').text = row[3]

    # Create a pretty-printed XML string
    xml_string = ET.tostring(root, encoding='utf-8')
    xml_pretty_string = minidom.parseString(xml_string).toprettyxml(indent="  ")

    # Write the XML to a file
    with open(xml_file, 'w') as xml_output:
        xml_output.write(xml_pretty_string)

# Replace 'input.csv' and 'output.xml' with your file paths
csv_to_rss('/Users/kurtdostal/Documents/GitHub/psychic-octo-adventure/input2.csv', '/Users/kurtdostal/Documents/GitHub/psychic-octo-adventure/output2.xml')
