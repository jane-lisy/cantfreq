#loading packages
import jieba
import xlsxwriter
import collections

print("Please read the code and change directories accordingly (see line 9, 13, and 22).")

#setting up workbook
workbook = xlsxwriter.Workbook('hkcac_word.xlsx')
worksheet = workbook.add_worksheet('words')

#read and segment sentences
with open("hkcac_sentences.txt", encoding = 'utf8', errors = 'backslashreplace') as f_in: #not provided, a csv of the corpus in the format: [chinese sentence], [phonetic representation]
    sents = list(line for line in (l.strip() for l in f_in) if line)
sents[0] = sents[0][1:]
jieba.load_userdict("hkcacmanual_words.txt")
orthos = []
for i in sents:
    orthos.extend(list(jieba.cut(i)))

#phono set up
df = read_csv("hkcac_char.csv", names=["Characters", "Phonos"]) #not provided, a csv of the corpus in the format: [chinese character], [phonetic representation]
characters = df.Characters.to_list()
phonos = df.Phonos.to_list()       

def word2phono(ortho):
    phono_compare = []
    match_count = len(ortho)
    for i in range(0, len(characters)-match_count):
        if ''.join(characters[i:i+match_count]) == ortho:
            phono_compare.append(phonos[i:i+match_count])
    try:
        return Counter([tuple(i) for i in phono_compare]).most_common(1)[0][0]
    except IndexError:
        return tuple([''.join(word2phono(i)) for i in ortho])

#word frequency
word_count = collections.Counter(orthos)

#writing data
row = 1
worksheet.write(0, 0, 'word')
worksheet.write(0, 1, 'phono')
worksheet.write(0, 2, 'occured')
worksheet.write(0, 3, 'ratio')

word_sum = sum(word_count.values())
for i in word_count.keys():
    worksheet.write(row, 0, i)
    worksheet.write(row, 1, word2phono(i))
    worksheet.write(row, 2, word_count[i])
    worksheet.write(row, 3, word_count[i]/word_sum)
    row += 1

workbook.close()