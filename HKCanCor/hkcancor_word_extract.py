#loading packages
import pycantonese as pc
import xlsxwriter
import collections

print("Please read the code and change directories accordingly (see line 9).")

#setting up workbook
workbook = xlsxwriter.Workbook('hkcancor_word.xlsx')
worksheet = workbook.add_worksheet('words')

#loading files
c = pc.hkcancor()

#getting words
tokens = c.search(tone = '[1-6]')

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
    worksheet.write(row, 0, i[0])
    worksheet.write(row, 1, i[2])
    worksheet.write(row, 2, word_count[i])
    worksheet.write(row, 3, word_count[i]/word_sum)
    row += 1

workbook.close()