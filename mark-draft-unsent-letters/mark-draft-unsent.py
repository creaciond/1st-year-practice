# черновые и неотправленные письма
# coding = utf-8
import xml.etree.ElementTree as ET
import os
import re


# def markUnsent(lPath):
    # regUnsent = re.compile('[Нн]еотправленное')
    # tree = ET.parse(lPath) 
    # root = tree.getroot()
    # title = root[0][0][0][0].text
    # isUnsent = re.search(regUnsent, title.encode('utf-8'))
    # if isUnsent:
        # root[0][2][0][0].attrib['type'] = 'unsent'
        # print(root[0][2][0][0].attrib)
        # print(title + ' 1')
        # tree.decode('utf-8')
        # tree.write(lPath)
    # print(title)



def markDraft(lPath):
    regDraft = re.compile('[Чч]ерновое')
    tree = ET.parse(lPath) 
    root = tree.getroot()
    title = root[0][0][0][0].text
    isDraft = re.search(regDraft, title.encode('utf-8'))
    if isDraft:
        root[0][2][0][0].attrib['type'] = 'draft'
        print(root[0][2][0][0].attrib)
        print(title + ' 1')
        tree.write(lPath)
    # print(title)
    


def main():
    # for i in range(59,90):
        # dirname = 'Volume_' + str(i)
        # for letter in os.listdir(dirname):
            # if letter.endswith('.xml'):
                # markDraft(dirname + os.sep + letter)    
                # markUnsent(dirname + os.sep + letter)
    for letter in os.listdir('Volume_59'):
        if letter.endswith('.xml'):
            markDraft('Volume_59' + os.sep + letter)
                

if __name__ == '__main__':
    main()