
vowelFile = open("vowel.txt" ,"r")
readData = vowelFile.read()

fileWordsSplit = readData.split()
print("this is line is to print words by spliting the sentence : ")
print()
print("Total words are : " ,len(fileWordsSplit) ,"in list ")