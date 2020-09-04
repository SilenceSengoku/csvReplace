#Author: Crow Lu
import os

def get_filelist(inputfile_dir):
    for root, dirs, files in os.walk(inputfile_dir):
        fileslist = files
        print(fileslist)
    return fileslist

def csv_replace(inputpath,outputpath):
    #power by https://blog.csdn.net/qq_44390640/article/details/103343090
    file = open(inputpath)

    content = file.read()
    file.close()
    # content = content.replace("要替换的值","期望替换的新值")
    content = content.replace("；", ",")
    content = content.replace("：", ",")
    with open(outputpath, "w", encoding='utf8') as line:
        line.write(content)

inputpath  = input('输入测试输入文件路径')
outputpath = input('输入测试输出文件路径')
#inputpath  = r'C:\Users\Administrator\PycharmProjects\checkreport\inputfiledir\csv'
#outputpath = r'C:\Users\Administrator\PycharmProjects\checkreport\output'
filelist = get_filelist(inputpath)

for line in filelist:
    csv_replace(inputpath+'/'+line,outputpath+'/'+line)

    print(line+' 替换完成')