# Переименовываем письма в папках

# encoding: utf-8 -*- 
import os
import re
import sys

	
def renamedir(dirname):
    # открыть каждый, найти название (тег text), переименовать,закрыть
    for each in os.listdir(dirname):
        if each.endswith('.xml'):
            letterpath = dirname+'/'+each
            letter = open(letterpath, 'r', encoding='utf-8')
            for line in letter:
                reg = re.search('<text xml:id=\"(.*?)\"', line)
                if reg:
                    name = reg.group(1)
                    os.rename(letterpath, dirname+'/'+name+".xml")
            letter.close()
    

def main():
    for i in range(59, 90):
        numstr = str(i)
        renamedir("Volume_"+numstr)
        # как только всё переименовано,маякнуть об этом
        print(numstr)   


if __name__ == '__main__':
	main()
