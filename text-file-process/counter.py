import os

counter = 0

for files in os.walk(r'C:\Users\95123\Desktop\text-file-process-ididChan\text-file-process\log_files'):
    for file in files:
        stu = file.split(',')[1]
        stu_id = stu[13:]
        if stu_id == '29':
            counter += 1
print(counter)
