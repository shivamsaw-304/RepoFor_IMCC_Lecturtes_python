vowelFile = open("vowel.txt" ,"r")
readData = vowelFile.read()

var = readData
count =  0

for i in var :
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"  :
      count += 1
print(readData)
print("the totall vowel present in file vowel.txt are : " ,count)

vowelFile.close()

# -----------------------------------------------------------------------------------------
fileForList= open("fileForList.txt", "r")
varOfFileForList  = fileForList.readlines()
count= 0
for li in varOfFileForList :
   count += 1
  
print("total line are present in fileForList.txt : " , count)
print()
print("------------------printing of 2 lines 2 and 4 ------------------------------------- ")
count = 0 
for li in varOfFileForList :
   count += 1
   if count == 2 or count == 4 :
      print(li )

fileForList.close()








# -------------------------------------------------------------Take a sentence from the user, split it into words, and store them in a list. Print the longest word.--------------------

userInput = input("Enter a sentence: ")

words = userInput.split()

longestWord = ""

for word in words:
    if len(word) > len(longestWord):
        longestWord = word

print("Words List:", words)
print("Longest Word:", longestWord)
print()




# Read a file, split its content into words, and store them in a list.Print the total number of words. Print all unique words.

vowelFile = open("vowel.txt" ,"r")
readData = vowelFile.read()

fileWordsSplit = readData.split()
print("this is line is to print words by spliting the sentence : ")
print()
print("Total words are : " ,len(fileWordsSplit) ,"in list ")