import xml.etree.ElementTree as ET
import os
'''
#xml helpme###에 대해서:
#경로 불러오기
for
    #name.set('updated', 'yes')
#동일한 파일명으로 저장?
       
        print(root)
        
        
'''



a="/home/wonsub/Desktop/1111"
b=os.listdir(a)
path = os.getcwd()
print(path)
for c in b:
    if c.endswith(".xml"):     
        path_xml=a+"/"+c
        tree = ET.parse(path_xml)
        root = tree.getroot()
        for name in root.iter('name'):
            print(name[0])
            '''
            new_name = "b"
            name.text = str(new_name)
            tree.write(c)
            '''
        
       
        