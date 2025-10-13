'''
    The same can be written using with statement and don't  have to explicitly close the code
'''

with open("D6_File_i-o/text.txt") as f:
    print(f.read())