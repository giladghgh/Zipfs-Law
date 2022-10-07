import xml.etree.ElementTree as ET
import string
import os,io

# Recurse through every file in the directory.
for d in ['aca','fic','news','spo']:
    parent = 'Raw/' + d

    with io.open('{}.txt'.format(d), 'w+', encoding='utf-8') as cleanfile:
        for n,f in enumerate(os.listdir(parent)):
            tree = ET.parse(parent + '/' + f)
            root = tree.getroot()



            # Print the whole doc verbatim.
            #print(ET.tostring(root, encoding='utf8').decode('utf8'))

            # Extract source document name.
            try:
                title = root.find('teiHeader/fileDesc/sourceDesc/bibl/title').text.strip()
                print(title,d,f)
            except:   pass

            # Parse the British National Corpus please mate.
            for word in root.iter('w'):
                w = word.attrib["hw"]
                if w.isalpha():   cleanfile.write(w + '\n')