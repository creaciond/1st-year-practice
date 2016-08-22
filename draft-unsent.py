# Разметка черновых и неотправленных писем

# encoding: utf-8
import os
import re


def markasdraft(dirname):
    re_draft = '<title>(.*)?[Чч]ерновое'
    re_unsent = '<title>(.*)?[Нн]еотправленное'
    for each in os.listdir(dirname):
        if each.endswith('.xml'):
            letterpath = dirname+'/'+each
            letter = open(letterpath, 'r+', encoding='utf-8')
            for line in letter:
                if '<title>' in line:
                    isdraft = re.search(re_draft,  line)
                    isunsent = re.search(re_unsent, line)
                if ('correspAction type=\"sending\"' in line) and (isdraft or isunsent):
                    if isdraft:
                        line.replace('sending','draft',1)
                    elif isunsent:
                        line.replace('sending','unsent',1)
            letter.close()

                
def main():
    for i in range(59, 90):
    numstr = str(i)
    markasdraft("Volume_"+numstr)


if __name__ == '__main__':
    main()
