# code block of Creating Node and Linked List
#  creation of node block 
class Node : 

    def __init__(self,value):
        self.value = value
        self.next = None


# creation of link list and implementatiion of codes of questions
class singliLinklist :

    def __init__(self):
        self.head = None
        self.count = 0
    
 # insetion of node to the specific position 
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
    
  # Traversaal of singli Link list and printing data of link list values 
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
        
        print("mid value of link list " ,tempNode.value)


    def deleteAtPosition(self, userPosition = 0):
         
        if self.head is None:
         print("Linked List Empty")
         return

        if userPosition > self.count or userPosition <= 0:
         print("Invalid Position")
         return

       # delete first node
        if userPosition == 1:
         self.head = self.head.next
         self.count -= 1
         return
 
        currentPosition = 2
        tempNode = self.head

        while currentPosition != userPosition:
         currentPosition += 1
         tempNode = tempNode.next

        tempNode.next = tempNode.next.next
        self.count -= 1
        print("node deleted succes fully " )
        sLObj.printLinkList()

    def reverseLinkList(self):

     previousNode = None
     currentNode = self.head

     while currentNode != None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

     print("reverse of link list")
     self.head = previousNode

    def sumOfConsecutiveNodes(self):

     tempNode = self.head
     print("the sum odf 2 consecutive  nodes of link list")

     while tempNode != None and tempNode.next != None :
        print(tempNode.value + tempNode.next.value)
        tempNode = tempNode.next

    def deletFirstAndLastNode(self):
       tempNode = self.head
       self.head = self.head.next
       if self.head == None:
          print("head is empty it conatains none value ")
          return 

       while tempNode.next.next != None :
          tempNode = tempNode.next
    
       tempNode.next = None
      
       return self.head
    

      
          
          
       
   







        


# program for insertion of ss linklist

sLObj = singliLinklist()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


sLObj.insetAtPosition(node1,1)
sLObj.insetAtPosition(node2,2)
sLObj.insetAtPosition(node3,3)
sLObj.insetAtPosition(node4,4)
sLObj.insetAtPosition(node4,5)

sLObj.findMiddelNode()
print(sLObj.deletFirstAndLastNode())

# sLObj.insetAtPosition((node1))
# sLObj.printLinkList()
# print(sLObj.count)
# sLObj.insetAtPosition((node3))
# sLObj.printLinkList()
# print(sLObj.count)
# sLObj.insetAtPosition(node2,2)
# sLObj.printLinkList()
# # print(sLObj.count)

# sLObj.findMiddelNode()
# # sLObj.deleteAtPosition()
# # sLObj.deleteAtPosition(2)
# sLObj.reverseLinkList()
# sLObj.printLinkList()

# sLObj.sumOfConsecutiveNodes()





