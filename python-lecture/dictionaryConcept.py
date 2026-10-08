import random


studentDict = {
    101:{"name" : "shivam" , "score" : [106,32,320]},
    102:{"name" : "shiva" , "score" : [103,342,320]},
    103:{"name" : "sarvesh" , "score" : [105,322,332]},
    104:{"name" : "ajay" , "score" : [106,325,320]},
    105:{"name" : "shivam" , "score" : [104,32,320]}
}

# for stuId , stuDet in studentDict.items():
#     avg= sum(stuDet["score"])// len(stuDet["score"])

#     stuDet["average"] = avg

# print(studentDict.items("/n"))


# userInput  = int(input("enter your guess number from 1 t0 10 : "))

# domNum  = random.randint(1,10)


# if (domNum == userInput):
#     print("Your guess is correcgt ")
# else:
#     print("try again !!")



# libraryDict  = {
    
# }

# clintName = input("enter your name ")

# newList = ["shiv" ,  "mahesh " , "bhola" ,"distroyer","om"]

# domNum  = random.randint(1,len(newList)-1)
# if clintName == "shivam":
#         print("its your name meaning  :  " + newList[domNum])
# else:
#         print("enter your correct name ")

# list of number and string accept from user seprate the list from the maximun number dispaly the name is desec order

numberOfData = int(input("enter number of data you have to enter  :"))
hexaList = []

for i in range(numberOfData):
    userInput = input("enter niumber and leter you  have to enter : ")

    list