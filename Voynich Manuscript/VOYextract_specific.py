import string
import os,io

pagetext = ['1r','39v','87r','103r','114v']

# 6 files to go through.
for p in range(5):
    P = pagetext[p]
    L = len(P)
    page = []

    # Find.
    with open('v101_{}.txt'.format(p+1),'w+',encoding='utf-8') as cleanfile , open('v101_raw.txt','r') as sourcefile:
        for line in sourcefile:
            if line[2:2+L] == P:
                chunk = line.split()[1]
                frag = chunk.split('.')
                page += frag
                for word in frag:
                    if ',' in word:
                        word = word.replace(',','\n')
                    cleanfile.write(word + '\n')

    # Clean.
    del page[0]

    # Out.
    print(p,page)