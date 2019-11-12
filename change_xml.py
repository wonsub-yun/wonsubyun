import xml.etree.ElementTree as ET
import os
original_directory="/home/wonsub/Desktop/1111"
list_of_files=os.listdir(original_directory)
for xml_files in list_of_files:
    if xml_files.endswith(".xml"):     
        path_xml=original_directory+"/"+xml_files
        tree = ET.parse(path_xml)
        root = tree.getroot()
        for name in root.iter('name'):
            new_name = "b"
            name.text = str(new_name)
            os.chdir(original_directory+"/")
            tree.write(xml_files)
        
       
        