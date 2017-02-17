import os
import glob
import time

print(os.getcwd())

os.chdir('/')
print(os.getcwd())

os.chdir('/Python34')
print(os.getcwd())

file_list=glob.glob('*.exe')
print(file_list)

print(os.path.join('/Python27',file_list[1]))

print(os.path.realpath(file_list[1]))


file_meta_data=os.stat(file_list[1])

print(file_meta_data.st_mtime)
print(file_meta_data.st_size)
print(file_meta_data.st_mode)
print(file_meta_data.st_dev)

