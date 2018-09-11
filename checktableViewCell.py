#!/usr/bin/python
#coding=utf-8

import os
import fnmatch
import itertools
import re
import json


PROJECT_PATH = ['../../']
OVERSEA_KEYWORD = r'_hod_'
INLAND_KEYWORD = r'_hoi_'


def find_files(pattern, path):
    """出所有的 .m 文件"""

    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            filepath = os.path.join(root, filename)
            yield filepath
            pass
        pass


def scan_files(source_files):
    """扫描文件，找出所有的 ab code"""

    source_function_list = []
    for file in source_files:
        # 逐行读取每个文件，查询匹配结果
        source_file_handle = open(file)
        source_file_lines = source_file_handle.readlines()

        for source_file_line in source_file_lines:
            oversea_re = r"@interface(.*?):(.*?)Cell"
            oversea_patten = re.compile(oversea_re)
            match_oversea = oversea_patten.search(source_file_line)
            if match_oversea and (match_oversea.group() not in source_function_list):
                    source_function_list.append(match_oversea.group())

            pass
        pass
    pass

    source_function_list.sort()
    # print "total:   len(source_function_list)

    return source_function_list





def check_source():
    """数据采集的入口函数"""

    alist = []
    # 遍历指定目录下的子目录
    for target_list in PROJECT_PATH:

        # 找出所有的 .m 文件
        source_files = [file for file in itertools.chain(find_files("*.h", target_list))]

        # 排序
        # source_files.sort()

        # 扫描文件获取其中的 AB code
        # 
        ab_item_list = scan_files(source_files)
        alist += (ab_item_list)
        # 获取各 AB 实验的详细信息
        
    currentCellArr=[]
    for i in alist:
        i = i.split(':', 1)[0]
        i = i.split('@interface', 1)[1]
        currentCellArr.append(i.strip(' \t\n\r'))
    
    oriCellArr=[]
    
    str_dump=[]
    fa=open("allCell.txt",'r')
    for line in fa.readlines():
        line = line.strip(' \t\n\r')
        oriCellArr.append(line.replace("\n",''))

    #将两个文件中重复的行，添加到str_dump中
    for i in currentCellArr:
        if i in oriCellArr:
            str_dump.append(i)
    
    for i in str_dump:
        if i in currentCellArr:
            currentCellArr.remove(i)
    
    if len(currentCellArr) > 0:
        print('有变动\n\n\n')
        print(currentCellArr)
        fc=open("all.txt",'w+')
        for i in list(currentCellArr):
            fc.write(i+'\n')
        fc.close()
    else:
        print('没有变动\n\n\n')


if __name__ == '__main__':
    check_source()
