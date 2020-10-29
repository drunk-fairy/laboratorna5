import csv
import os 

os.chdir('e:/University/University1/ICS-18092020/laboratorna5')

def isFileExisting(filename):
    return os.path.isfile(filename)

def outputFileByName(filename):
    print('File ' + filename)
    fd = open(filename, 'r')
    reader = csv.reader(fd, delimiter='\t')
    for row in reader:
        print(row)
    fd.close()

file1='first_group.py'
file2='second_group.py'

def readFiles():

    fd1=open(file1,'r')
    reader = csv.reader(fd1, delimiter='\t')
    print('\nfirst group:')
    for row in reader:
        print(row) 

    fd2=open(file2,'r') 
    reader = csv.reader(fd2, delimiter='\t')
    print('\nsecond group:')
    for row in reader:
        print(row) 

    fd1.close() 
    fd2.close()

def writeToFiles():
    fd1=open(file1,'w')
    fd1.write('Zelenskiy Andriy, 61\nIvanov Andriy, 82\nHolovanov Vitaliy, 93')

    fd2=open(file2,'w')
    fd2.write('Malaniuk Yevhen, 73\nRomanenko Mariya, 66\nSokolovska Alisa, 48')

    fd1.close() 
    fd2.close()

def addToFiles():
    fd1=open(file1,'a')
    fd1.write('\nMikhaylevskiy Maksim, 87\nBlizniuk Anna, 75\nBabich Karina, 53')

    fd2=open(file2,'a')
    fd2.write('\nRadchenko Stepan, 93\nBilous Andriy, 60')

    fd1.close() 
    fd2.close()

def searchFilesInDirectory(query):
    if(not isFileExisting(query)):
        print('File with name ' + query + 'does not exist')
    else:
        outputFileByName(query)

def searchTextInFiles(filename, query):

    fd = open(filename,'r')
    reader = fd.readlines()

    for row in reader:
        if query.lower() in row.lower():
            print(f'Found: {row}')

    fd.close()

def sortMarksInFile(filename):
    dict = {}

    fd = open(filename, 'r+')

    reader = fd.readlines()

    for row in reader:
        split_row_by_coma = row.split(',')

        dict[int(split_row_by_coma[1])] = split_row_by_coma[0]

    sorted_dict_by_items = sorted(dict.items())
    print(sorted_dict_by_items)
    fd.close()


#readFiles()
#writeToFiles()
#addToFiles()
#searchFilesInDirectory(file2)
#searchTextInFiles(file2, 'ous')
sortMarksInFile(file1)