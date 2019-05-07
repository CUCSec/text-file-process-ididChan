import os

counter = 0

path = r'C:\Users\95123\Desktop\text-file-process-ididChan\text-file-process\log_files'
files = os.listdir(path)
for file in files:
    with open(path + '//' + file,encoding='utf8') as f:
        for line in f:
            stu = line.split(',')[1]
            stu_id = stu[14:]
            if stu_id == '29':
                counter =counter + 1

print(counter)
