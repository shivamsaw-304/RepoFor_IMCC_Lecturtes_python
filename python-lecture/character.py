n = int(input("enter numbre : "))
asc = 65 # asci value of A (not a)

for i in range(n):
    for j in range(i+1
                   ):
        print(chr(asc + 1),end=" ")
    print()