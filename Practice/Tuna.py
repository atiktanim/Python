
fw=open('Sample.txt','w')
fw.write("I won't access to facebook in this year\n")
fw.write('InshAllah I wiil do that')
fw.close()
fr = open("Sample.txt","r")
text=fr.read()
print(text)
fr.close()