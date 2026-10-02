# # ----------------- first Python program -------------
# #UserInput = int(input("taking user in put : "))
# List = [1,2,3,4,5,6,7,8,9,3]
# Tuple = ()
# Dict = {"key":"value"}

# for i in range(len(List),-1,-1): # reversal travel
#     for j in range(len(List),-1,-1):
#          print(i ,end=" ")
#     print() 
  



n = int(input("Enter number : "))

for i in range(n):
    
    for j  in range(n):
        if j == n//2 or i == n//2 :
            print("*",end="")
        elif i!= n//2:
            print(end=" ")
    print()

     
        