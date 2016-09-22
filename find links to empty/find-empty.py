## coding: utf-8
import os


def isempty(lpath):
    letter = open(lpath, 'r', encoding='utf-8')
    linecount = 0
    for line in letter:
        linecount += 1
    if linecount <= 65:
        return 1
    else:
        return 0
    letter.close()


def returnempty(dirname):
    for each in os.listdir(dirname):
        if each.endswith('.xml') and ('S__A__Tolstoj' in each or 'CHertkovu' in each):
            lpath = dirname + '/' + each
            if isempty(lpath) == 1:
                print(lpath)
            
        

def main():
    for i in range(59,84):
        numstr = str(i)
        returnempty('Volume_'+numstr)    


if __name__ == '__main__':
    main()
