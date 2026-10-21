# *args = tuple , **kwargs = dictionary

def argsType(*listOfString):
    if len(listOfString) == 0:
        return None

    maxStringlength = 0
    maxWord = ""


    for i in range(len(listOfString)):

        if len(listOfString[i]) > maxStringlength :
            maxStringlength = len(listOfString[i])
            maxWord = listOfString[i]

    return maxWord,maxStringlength


print(argsType("shivam", "saw","hi " ,"           " ))




