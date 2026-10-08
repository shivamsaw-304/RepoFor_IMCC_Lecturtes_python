thisIsList = [4,2,1,34,2,3,34,67,35,75,35,853,75,356,366787,45,6,4567,67,35]

# methods for lsit - lsit.append() , list.remover()  - takes argument ,list.pop()  , 

#  create a list of 10 numbrs print the sum of last 4 elements of the list  , find out the difference of max and min of the list  , insert a item in a list at 6th positon this number must be 1/3rd  off number stored at 4th  position
#  function - sorted() 3 arguments leta hain (list/ string ,  key = non , reverse = true ) 
print(sorted(thisIsList)) 

print(thisIsList)




#  create a list of 10 numbrs print the sum of last 4 elements of the list  , find out the difference of max and min of the list  , insert a item in a list at 6th positon this number must be 1/3rd  off number stored at 4th  position

questList = [32,43,23,54,23,54,123,53,43,23]
length = len(questList)
count = 0
sum = 0
for i in questList :
    if(count >=  length - 4):
        sum = i + sum
    count += 1
print(sum)

funSum = questList[-1]+questList[-2]+questList[-3]+questList[-4] 
print(funSum)
print(max(questList))
print(min(questList))













