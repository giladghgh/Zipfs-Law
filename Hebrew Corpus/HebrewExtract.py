import xml.etree.ElementTree as ET
import string
import os,io

# Recurse through every file in the directory.
with io.open('HebrewWiki.txt', 'w+', encoding='utf-8') as cleanfile:
    parent = 'Raw'
    for n,f in enumerate(os.listdir(parent)):
        tree = ET.parse(parent + '/' + f)
        root = tree.getroot()

        # Print the whole doc verbatim.
        #print(ET.tostring(root, encoding='utf8').decode('utf8'))

        # Parse the Hebrew MILA Corpus please mate.
        for word in root.findall('.//token/analysis[@id="1"]'):
            for token in word:
                if token.tag == 'prefix':
                    h = token.attrib['surface']
                    if h.isalpha():   cleanfile.write(h + '\n')
                elif token.tag == 'base':
                    try:
                        h = token.attrib['lexiconItem']
                        if h.isalpha():   cleanfile.write(h + '\n')
                    except:   pass