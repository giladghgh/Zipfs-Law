import string
import os,io

pagetext = ['1r','39v','87r','97v','101v']

# Find.
with open('v101_wholeclean.txt','w+',encoding='utf-8') as cleanfile , open('cleaned.txt','r') as sourcefile:
    for line in sourcefile:
        frag = line.split('.')

        for word in frag:
            cleanfile.write(word + '\n')