'''Reading the file'''

f = open("D6_File_i-o/text.txt", "r")
data = f.read()
print(data)
f.close()


'''Writing or creating new file'''
new = "I am learning Python"

wt = open("D6_File_i-o/writing.txt", "w")
wt.write(new)
wt.close()


'''More functions'''
f1 = open("D6_File_i-o/text.txt")
data1 = f1.readline()
print(data1)

data2 = f1.readline()
print(data2)
f1.close()