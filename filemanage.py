'''FileIntroduce:这个文件主要是用来实现拷贝文件，拷贝文件夹，新建，删除文件等os操作'''
#author:ytouch
#date:2019/4/26
#using suggestion: 包含路径的参数均为绝对路径，因为要使得该py文件具有通用性
 
import os
import shutil
from shutil import copyfile
 
cur_file_name = '' #设定该变量为全局变量，表示当前文件名，用于copyFileToFolder方法中
 
'''Func:在指定路径下新建文件夹功能'''
def newFolderpath(folder_path):
    #param1:指定新建文件夹路径
    is_Exist = os.path.exists(folder_path) #判断该文件夹是否存在
    if not is_Exist: #不存在时创建该文件夹
        os.mkdir(folder_path)
    else:
        print("当前文件夹已存在，文件夹路径为：" + folder_path)
 
'''Func:新建任意后缀文件'''
def newFile(new_file_path):
    #param1:新建的文件路径
    cur_file = open(new_file_path,'w')
    cur_file.close()
 
'''Func:复制文件到指定文件路径下'''
def copyFileToFile(file_path,new_file_path):
    #param1:需要复制的文件路径
    #param2:指定的文件路径下
    copyfile(file_path,new_file_path)
 
'''Func:复制文件到指定文件夹路径下'''
def copyFileToFolder(file_path,new_folder_path):
    #param1:需要复制的文件路径
    #param2:指定的文件夹路径下
    global cur_file_name
    if file_path.find('/') >= 0: #判断路径格式 / or \\
        list_file_path = file_path.split('/')
        cur_file_name = list_file_path[len(list_file_path)-1] #取出对应文件名
    else:
        list_file_path = file_path.split('\\')
        cur_file_name = list_file_path[len(list_file_path)-1]
    if new_folder_path.find('/') >= 0: #判断路径格式 / or \\
        if new_folder_path.endswith('/'):
            new_copy_path = new_folder_path + cur_file_name
            copyfile(file_path, new_copy_path)
        else:
            new_copy_path = new_folder_path + '/' + cur_file_name
            copyfile(file_path, new_copy_path)
    else:
        if new_folder_path.endswith('\\'):
            new_copy_path = new_folder_path + cur_file_name
            copyfile(file_path, new_copy_path)
        else:
            new_copy_path = new_folder_path + '\\' + cur_file_name
            copyfile(file_path,new_copy_path)
 
'''Func:复制文件夹到指定文件夹路径下:(并且包含里面的文件)'''
def copyFolderToFolder(folder_path,new_folder_path):
    #param1：需要复制的文件夹路径
    #param2: 新的文件夹路径
    if not os.path.exists(folder_path):
        print("folder_path not exist!")
    if not os.path.exists(new_folder_path):
        print("new_folder_path not exist!")
    for root,dirs,files in os.walk(folder_path,True):
        for eachfile in files:
            shutil.copy(os.path.join(root,eachfile),new_folder_path)
 
'''Func:删除指定空的文件夹'''
def deleteEmptyFolder(folder_path):
    #param1:需要删除的空的文件夹路径
    os.rmdir(folder_path)
 
'''Func:删除包含文件内容的文件夹'''
def deleteFolder(folder_path):
    #param1:需要删除的文件夹路径
    shutil.rmtree(folder_path,True)
 
'''Func:删除指定的文件'''
def deleteFile(file_path):
    #param1:删除文件的路径
    is_Exist = os.path.exists(file_path) #先判断是否该文件存在
    if not is_Exist:
        print("当前文件路径不存在")
    else:
        os.remove(file_path)