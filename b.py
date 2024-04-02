import os
import datetime
import math

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

    print(f'root={root}')
    print(f'route={route}')
    print(f'dir={dir}')


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
