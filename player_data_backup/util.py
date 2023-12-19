import os
import re
def get_all_file(target:str,pattern:str):
    res = []
    if os.path.isdir(target) == False:
        res.append(target)
        return res

    files = os.listdir(target)
    for f in files:
        if re.match(pattern,f):
            res.append(files)
                
    return res