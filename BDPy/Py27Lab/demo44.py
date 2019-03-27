import shutil
path1='source'
path2='clone'
shutil.copytree(path1, path2)
shutil.rmtree(path2)