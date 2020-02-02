import xml.etree.ElementTree as ET

tree=ET.parse("phonebook.xml")

container=tree.find("entries")
data=[]
for elem in container:
    key = elem.findtext("number")
    data.append(key,elem)

data.sort()
container[:] = [item[-1] for item in data]
tree.write("new_phonebook.xml")