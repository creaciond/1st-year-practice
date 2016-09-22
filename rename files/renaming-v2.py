# Переименовываем письма в папках

# encoding: utf-8 -*- 
import os
import re
import sys

	
def renamedir(dirname):
    for each in os.listdir(dirname)[1::]:
        path = dirname+'/'+each
        for l in os.listdir(path):
            if l.endswith('.xml'):
                letter = open(path+'/'+l, 'r', encoding='utf-8')
                for line in letter:
                    reg = re.search('<text xml:id=\"(.*?)\"', line)
                    if reg:
                        name = reg.group(1)
                        os.rename(path+'/'+l, path+'/'+name+".xml")
                letter.close()


def main():
    for i in range(59, 90):
        numstr = str(i)
        renamedir("Volume_"+numstr)
        # как только всё переименовано,маякнуть об этом
        # print(numstr)   


if __name__ == '__main__':
	main()
