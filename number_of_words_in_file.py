# Task 4.2

from pathlib import Path
import os
import csv

os.chdir('e:/University/University1/ICS-18092020/laboratorna5')

book = 'Тарас Шевченко. Катерина.txt'
test = 'петрарка.txt'

def numberOfCharsWithSpaces():
    file = open(book, 'r', encoding = 'utf-8')
    s = file.read()
    num = len(str(s))
    print('number of chars with spaces: ' + str(num))
    file.close()

# Alternative way: 
def numberOfCharsWithSpaces2():
    print(len(Path(book).read_text(encoding = 'utf-8')))

def numberOfCharsNoSpaces():
    file = open(book, 'r', encoding = 'utf-8')
    s = file.readlines()
    n = 0
    for row in s:
        for symbol in row:
            if symbol != ' ' and symbol != '\n':
                n += 1
        
    print('number of chars without spaces: ' + str(n))

def numberOfWordsInText():
    file = open(book, 'r', encoding = 'utf-8')
    s = file.readlines()

    # Counting the number of words, 
    # but empty lines and dashes are counted as words, too
    c = 0
    for row in s:
        words = row.split(' ')
        c = c + len(words)

    # Counting the number of empty lines: 
    n = 0
    for row in s:
        if row == '\n':
            n += 1

    # Counting the number of dashes:
    d = 0
    for row in s:
        for symbol in row:
            if symbol == '—':
                d += 1

    # The actual number of words:
    print('number of words: ' + str(c-n-d))
    #print(c)
    #print(n)
    #print(d)

def numberOfDifferentWords():
    a = len(set(Path(book).read_text(encoding = 'utf-8').split()))
    s = set(Path(book).read_text(encoding = 'utf-8'))
    n = 0
    for symbol in s:
        if symbol == '—':
            n = 1
    # We substract n=1 because dash ('—') is also counted, but it is not a word
    print('number of different words: ' + str(a-n))

def numberOfUniqueWords():
    unique_words = set()
    wordlist = Path(book).read_text(encoding = 'utf-8').split()
    for i in range (0, len(wordlist)):
        if(wordlist.count(wordlist[i]) == 1):
            unique_words.add(wordlist[i])
    print('number of unique words: ' + str(len(unique_words)))



# Task 4.3
# Варіант 1. Знайдіть у тексті найдовшу послідовність слів, що повторюється більше одного разу.

#def longestSequence():
    #wordlist = Path(test).read_text(encoding = 'utf-8').split()
    #repeated = []
        ##for i in range (0, len(wordlist)):
        ##word = wordlist[i]
    #i = 0
    #wordlist = []
    #word = worldist[i]
    #while i <= len(wordlist):
        #if(wordlist.count(word) > 1):
            #word = word + wordlist[wordlist.index(word) + 1]
            #repeated.append(word)
        #else:
            #word = wordlist[wordlist.index(word) + 1]
    #print(repeated)  

numberOfCharsWithSpaces()
numberOfCharsWithSpaces2()
numberOfCharsNoSpaces()
numberOfWordsInText()
numberOfDifferentWords()
numberOfUniqueWords()
#longestSequence()
