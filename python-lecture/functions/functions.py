
#key value parameters only (* on begin of parameter )
def giveReminder(* ,num , deno):
    return num % deno



# position only parameter only (/ on last of parameter )

def onlyPositonParameter(position , positionn2 ,/):
    print("thank you for entering argument onliy in position basis : !! ")

def onlyKeyValueParameter(*,key , key1 ):
    print("thank you fro entering only key values argumeny : !! ")


num = int(input("enter numetrator for devision : "))
denominator = int(input("enter denominator : "))

print("the reminder of given input from the user : " , giveReminder(num= num, deno= denominator))

onlyKeyValueParameter()
onlyPositonParameter()




