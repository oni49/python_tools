import os

dir = './mydir/'
for filename in os.listdir(dir):
    name, ext = filename.strip(' \n').split('.')
    parts = name.split(' ')
    date, last_name, title = parts[0], parts[1], '-'.join(parts[2:])
    new_filename = '_'.join([last_name, title, date])+'.'+ext
    os.rename(dir+filename, dir+new_filename)
