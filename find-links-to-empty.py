## coding: utf-8
import os
import re

def findlinks(lpath):
    letter = open(lpath, 'r', encoding='utf-8')
    for line in letter:
        haslink = 'См\. письм[ао]: '
        if re.search(haslink, line):
            hasTolstaya = 'С\. А\. Толстой'
            hasChertkov = 'В\. Г\. Черткову'
            if re.search(hasTolstaya, line) or re.search(hasTolstaya, line) 
                return 1
    letter.close()


def showlinks(dirname):
    for each in os.listdir(dirname):
        if each.endswith('.xml'):
            lpath = dirname + '/' + each
            if findlinks(lpath) == 1:
                print(lpath)
        


def main():
    for i in range(59,83):
    # до 83 тома — с него начинаются письма Толстой и Черткову,
    # ссылки на которые мы и ищем
        numstr = str(i)
        showlinks('Volume_'+numstr)    


if __name__ == '__main__':
    main()
