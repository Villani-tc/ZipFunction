# .py que separa um conjunto de arquivos em pastas diferentes depois Zipa os dados contidos nas pastas.

import zipfile
import os
import glob
import shutil


def path_exists(path):       #Define um Path, se ele não existir, cria
    if not os.path.exists(path):
        os.makedirs(path)
        print(path + ' Created')   


def path_care():
    path_exists('Insira o Path')


def Allocation_Plus_Zip():
    path_care()
    direct_data = 'C:\Cloud\Data\Zipped\Data'
    direct_domain = 'C:\Cloud\Data\Zipped\Domain'
    direct_main = 'C:\Cloud\Data'

    data_main = glob.glob(str(direct_main) + '/*.csv', recursive=True)
    for file in data_main:
        file_split = file.split('\\')
        file_split = file_split[-1]
        if 'Doma' == file_split[0:4]:
            shutil.move(file, direct_domain)
        else:
            shutil.move(file, direct_data)
    os.chdir(direct_data)
    files_da = glob.glob(str(direct_data) + '/*.csv', recursive=True)
    files_do = glob.glob(str(direct_domain) + '/*.csv', recursive=True)

    with zipfile.ZipFile("DataZip.zip", "w", compression=zipfile.ZIP_DEFLATED) as myzip:
        for file in files_da:
            file_split = file.split('\\')
            file_split = file_split[-1]
            myzip.write(file_split)
            os.remove(file)

    os.chdir(direct_domain)
    with zipfile.ZipFile("DomainZip.zip", "w", compression=zipfile.ZIP_DEFLATED) as myzip:
        for file in files_do:
            file_split = file.split('\\')
            file_split = file_split[-1]
            myzip.write(file_split)
            os.remove(file)


def ZipFile_Permission():
    direct_data = 'C:\Cloud\Data\Zipped\Data'
    os.chdir(direct_data)
    while os.path.isfile("DataZip.zip"):
        wait = True


def Data_Direct_Permission(function):
    direct_main = 'C:\Cloud\Data'
    os.chdir(direct_main)
    if os.path.isfile('End.txt'):
        return function


path_care()
Allocation_Plus_Zip()
