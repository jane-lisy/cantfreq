#loading packages
import os
import xlsxwriter
import collections
import re

print("Please read the code and change directories accordingly (see line 10, 14, and 21).")

#setting up workbook
workbook = xlsxwriter.Workbook('iarpa_word.xlsx')
worksheet = workbook.add_worksheet('words')

#loading files
os.chdir("~\\transcript_roman") #change directory to the folder with all english transcripts

#getting words
tokens = []
for filename in os.listdir(os.getcwd()):
    if filename != '._':
        ro_file = open(filename, "r")
        chin_address = '~\\transcript_chin\\' + filename
        chin_file = open(chin_address, "r", encoding = "utf8", errors = "backslashreplace")

        ro_content = ro_file.read()
        chin_content = chin_file.read()

        ro_list = ro_content.split()

        chin_list = chin_content.split()

        tokens.extend(list(zip(ro_list, chin_list)))

delim = ['<', '(', '[', '~']

count = 0
while count < len(tokens):
    if tokens[count][0][0] in delim:
        try:
            if tokens[count+2][0][0] in delim:
                del tokens[count+1]
        except IndexError:
            pass
    count += 1

tokens = [i for i in tokens if i[0][0] not in delim]

count = 0
while count < len(tokens):
    try:
        if '-' in tokens[count+1][0] or '-' in tokens[count-1][0]:
            if tokens[count][0] in 'a1-a1a3a3-m4m4-':
                del tokens[count]
    except IndexError:
        pass
    count += 1

tokens = [i for i in tokens if sum(isEnglish(c) for c in i[1]) == 0]

#word frequency
word_count = collections.Counter(tokens)

#writing data
row = 1
worksheet.write(0, 0, 'word')
worksheet.write(0, 1, 'jyutping')
worksheet.write(0, 2, 'occured')
worksheet.write(0, 3, 'ratio')

word_sum = sum(word_count.values())
for i in word_count.keys():
    worksheet.write(row, 0, i[1])
    worksheet.write(row, 1, i[0])
    worksheet.write(row, 2, word_count[i])
    worksheet.write(row, 3, word_count[i]/word_sum)
    row += 1

workbook.close()