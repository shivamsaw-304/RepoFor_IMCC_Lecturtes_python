thisIsString = "hi this is  string sdfd asfarf wedwe dfgrt asdf asdfer"


#string methods and function are used

#method 
thisIsString.strip() 
# thisIsString = "hi this is  string sdfd asfarf wedwe dfgrt asdf asdfer"
print(thisIsString.partition("this")) # it defaultlu partition in to 3 string
# ('hi ', 'this', ' is  string sdfd asfarf wedwe dfgrt asdf asdfer')
#    1   ,  2   ,             3

# functon - len(ArgString ) this is fution taht takes  argument and restrun length of string argument which is passed 
print(len(thisIsString))
# 54


# function - str() takes parameter of non string typpe and convert it into string 
numerStr = [33,33,423,553,23,54,578,54,87,97,65,987,557,7885,46,876,46,89]
print(str(thisIsString))
print(str(numerStr) + thisIsString)



#   functon  - ord() it takes parameter as character and returns its ascii value no String is accept in parameter 
# print(ord(thisIsString) , ord(numerStr))
asciiVAl = ord("a")
print(ord("a"))
print(asciiVAl)
se="u"

# print(se)

# print(sorted(numerStr ,key=abs))


print(repr(numerStr))

#function 

it  = "  wehfiorhoih  " 
format = " --format--  "
evalution  = "200 + 32323 "
formatString = "this {} is now total {}".format(it,format)
print(formatString)
print(eval(evalution)) # for calculative operation evall() iss use 

# ----------------------------- METHODS -----------------------------------------------------------


defaultString = "shivam is default string "

isUpper  = defaultString.upper() # no argument is passed to it teh only thing is done to do upper case  and the modified stri ng is return 

print(isUpper) 