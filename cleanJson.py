import json
import re
fread = open("ML_Practice_Exam_Questions_ml.json", "r")

fwrite = open("nullLess.json","w")

contents = fread.read()

#contents = "<br />".join(contents.split("\n"))
cleanNewContents = contents.replace("–", "-").replace('—', '-').replace('…', '...').replace('‚', ',').replace('„', '"').replace('‘', "'").replace("’", "'").replace('›', '>').replace('©', '').replace('«', '<<').replace('®', '').replace('¯', '').replace('°', ' degrees').replace("´", "'").replace('»', '>>').replace('×', 'x').replace('÷', '/').replace('¼', '1/4').replace('½', '1/2').replace('¾', '3/4').replace('“', '"').replace('”', '"').replace('ˆ', '^').replace('€', ' pounds').replace('™', ' trade mark').replace("'", '')

print("contents lenth: ", len(contents))
print("cleanContents length: ", len(cleanNewContents))

nullCount = contents.count('–')
print("null count: ", nullCount)

fwrite.write(cleanNewContents)
fwrite.close()