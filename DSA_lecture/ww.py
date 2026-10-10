
class Node : 

    def __init__(self,value):
        self.value = value
        self.next = None

class singliLinklist :

    def __init__(self):
        self.head = None
        self.count = 0
    

    def insetAtPosition(self ,newNnode, userPosition = None ):


        if self.head is None:
            self.head = newNnode
            self.count += 1
            return self.head

        if userPosition == 1 or userPosition is None:
            newNnode.next =  self.head
            self.head = newNnode
            self.count += 1
            return self.head

        currentPosition = 2
        tempNode = self.head

        while currentPosition != userPosition:
            currentPosition += 1
            tempNode = tempNode.next

        newNnode.next = tempNode.next
        tempNode.next = newNnode
        self.count += 1 

        return self.head

    def printLinkList(self):
        tempNode = self.head

        while tempNode != None:
            print(tempNode.value , end="--> ")
            tempNode = tempNode.next
        print()

    def findMiddelNode(self):
        tempNode = self.head
        linkListsize = self.count
        countingSize = 0

        while(countingSize < linkListsize//2):
            tempNode = tempNode.next
            countingSize += 1

        if linkListsize % 2 == 0 :
            print(tempNode.data)
        else:
            tempNode = tempNode.next
            print(tempNode.data)







        


# program for insertion of ss linklist

sLObj = singliLinklist()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

sLObj.insetAtPosition((node1))
sLObj.printLinkList()
print(sLObj.count)
sLObj.insetAtPosition((node3))
sLObj.printLinkList()
print(sLObj.count)
sLObj.insetAtPosition(node2,2)
sLObj.printLinkList()
print(sLObj.count)

sLObj.findMiddelNode()





