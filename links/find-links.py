## coding: utf-8
import os
import re


def linksTolstaya(lpath):
    letter = open(lpath, 'r', encoding='utf-8')
    for line in letter:
        haslink = 'См\. письм[ао].*?к С(офье|\. ?)А(ндреевне|\.) Толстой'
        if re.search(haslink, line):
            return 1
    letter.close()


def linksChertkov(lpath):
    letter = open(lpath, 'r', encoding='utf-8')
    for line in letter:
        haslink = 'См\. письм[ао].*?В(ладимиру|\. ?)Г(ригорьевичу|\.) Черткову'
        if re.search(haslink, line):
            return 1
    letter.close()


def showlinks(dirname):
    for each in os.listdir(dirname):
        if each.endswith('.xml'):
            lpath = dirname + '/' + each
            if linksTolstaya(lpath) == 1:
                print("к Толстой", lpath)
            if linksChertkov(lpath) == 1:
                print("к Черткову", lpath)


def main():
    for i in range(59,83):
    # до 83 тома — с него начинаются письма Толстой и Черткову,
    # ссылки на которые мы и ищем
        numstr = str(i)
        showlinks('Volume_'+numstr)    


if __name__ == '__main__':
    main()
