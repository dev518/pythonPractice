#!/usr/bin/python
#coding=utf-8


import os
import fnmatch
import itertools
import re
import json
import sys

PROJECT_PATH = ['']


def find_files(pattern, path):
    arr = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(('.jpg', '.jpeg', '.gif', '.png')):
                arr.append(filename)
                pass
    
    return arr





def check_source():
    oriCellArr=[]
    
    fa=open("allCell.txt",'r')
    for line in fa.readlines():
        line = line.strip(' \t\n\r')
        oriCellArr.append(line.replace("\n",''))
    
    source_files = [file for file in itertools.chain(find_files(['*.jpg','*.png'], './resources'))]

    # sys.argv[0].replace('generateMD.py','')
    fc=open("README.md",'w+')
    for i in list(oriCellArr):
        for j in list(source_files):
            if i in j:
                fc.write('# '+i+'\n')
                imgPath = j.replace('./','')
                fc.write('![]('+imgPath+')\n')
                break
    fc.close()



if __name__ == '__main__':
    check_source()
