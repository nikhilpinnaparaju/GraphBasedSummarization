from xml.etree import ElementTree as ET
# enter file name here
tree = ET.parse("06_1.xml")
doc = tree.getroot()
sentences = doc.findall('sentences/sentence')
lst = []
for sentence in sentences:
	lst.append(sentence.text.replace('\n',''))
print(lst)