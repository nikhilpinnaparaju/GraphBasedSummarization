from xml.etree import ElementTree as ET
import os

for filename in os.listdir('../corpus/corpus/fulltext'):

# enter file name here
tree = ET.parse("../corpus/corpus/fulltext/06_3.xml")
doc = tree.getroot()
sentences = doc.findall('sentences/sentence')
# lst = []

f = open("../sample.txt","w")

for sentence in sentences:
	# lst.append(sentence.text.replace('\n',''))
	l = sentence.text.replace('\n','')
	f.write(l)

f.close()
# print(lst)

tree = ET.parse("../corpus/corpus/citations_summ/06_3.xml")
doc = tree.getroot()
phrases = doc.findall('citphrases/citphrase')

f = open("../annotated_keys.txt","w")

for phr in phrases:
	l = phr.text.replace('\n','')
	f.write(l)
	f.write("\n")

f.close()