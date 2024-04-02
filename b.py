# -*- coding: utf-8 -*-
import os
import datetime
import math
from zipfile import ZipFile

def get_type(filepath):
    if os.path.isdir(filepath):
        return "dir",'目录'
    elif os.path.isfile(filepath):
        if filepath.endswith('.sh'):
            return 'sh','shell脚本'
        elif filepath.endswith('.py'):
            return 'py','python文件'
        elif filepath.endswith('.cpp'):
            return "c++",'c++文件'
        elif filepath.endswith('.md'):
            return 'md','markdown文件'
        elif os.access(filepath, os.X_OK):
            return "exe",'可执行程序'
        else:
            return "txt",'文本文档'

def format_size(size_bytes):
    """
    Convert bytes to human-readable format
    """
    if size_bytes == 0:
        return "0"

    # Define units
    units = ['B', 'K', 'M', 'G', 'T']

    # Calculate exponent
    exp = min(int(math.log(size_bytes, 1024)), len(units) - 1)

    # Calculate value
    value = size_bytes / (1024 ** exp)

    # Format value and unit
    return "{:.1f} {}".format(value, units[exp])


def get_all(root,route,list_dot):
    files=[]
    
    dir=os.path.join(root,route)

    for f in os.listdir(dir):
        if list_dot==False:
            if f.startswith('.'):
                continue

        f_path = os.path.join(dir,f)
        type,cn_type = get_type(f_path)
        f_stat=os.stat(f_path)
        f_info={
            'type':type,
            'cn_type':cn_type,
            'name':f,
            'route':os.path.join(route,f),
            'size':format_size(os.path.getsize(f_path)),
            'change_date':datetime.datetime.fromtimestamp(f_stat.st_mtime).strftime('%Y-%m-%d %H:%M')
        }        
    
        files.append(f_info)

    return files



def zip_dir(pre_path,dir_name):
    path=os.path.join(pre_path,dir_name)
    with ZipFile(path+'.zip', 'w') as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path,path)
                zipf.write(file_path, arcname=relative_path)

    return path+'.zip'
