# class Node :

#     def __init__(self,value):
#         self.data= value
#         self.next = None


# class LinkList :

     
#     def __init__(self):
#          self.head = None
 



#     def insetAtFirst(self,newNode):

#         if self.head == None:
#             self.head = newNode 
#             return
#         else:
#             temp = self.head

#         newNode.next = temp
#         self.head = newNode


#     def insetAtSpecificPostion()


#     def  printLL(self):

#         temp = self.head

#         while(temp != None):
#             print(temp.data ,end="---> ")
 
#             temp = temp.next

#         print("non")

# node1 = Node(20)
# node2 = Node("shivam")
# node3  = Node(21)
# node4 = Node(22)

# ll = LinkList()

# ll.insetAtFirst(node1)
# ll.insetAtFirst(node2)
# ll.insetAtFirst(node3)

# ll.printLL()
        

class Node : 

    def __init__(self,value):
        self.value = value
        self.next = None

class singliLinklist :

    def __init__(self):
        self.head = None
    

    def insetAtPosition(self ,newNnode, userPosition =None):


        if self.head == userPosition :
            self.head == newNnode
            return self.head

        if userPosition == 1 or userPosition == None:
            newNnode.next =  self.head
            self.head = newNnode
            return self.head

        currentPosition = 2
        tempNode = self.head

        while currentPosition != userPosition:
            currentPosition += 1
            tempNode = tempNode.next

        newNnode.next = tempNode.next
        tempNode = newNnode

        return self.head

    def printLinkList(self):
        tempNode = self.head

        while tempNode != None:
            print(tempNode.data , end="--> ")
            tempNode = tempNode.next

        


# program for insertion of ss linklist

sLObj = singliLinklist()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

sLObj.insetAtPosition(node3)
sLObj.printLinkList()
sLObj.insetAtPosition(node2)
sLObj.printLinkList()







