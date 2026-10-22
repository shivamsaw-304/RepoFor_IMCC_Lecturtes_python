class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


class DdLL:



    def __init__(self):
        self.head = None
        self.last = None

    def insertionOfDll(self, newNode):

        if self.head == None:
            self.head = newNode
            self.last = newNode
            return self.head

        tempNode = self.head

        while tempNode.next != None:
            tempNode = tempNode.next

        newNode.prev = tempNode
        tempNode.next = newNode
        self.last = newNode
        return self.head
    

    def printDll(self):
        tempNode = self.head

        while tempNode :


            print(tempNode.data,end="<-->")
            tempNode = tempNode.next
        
        print("none")

    def occuranceOfNumber(self,num):

        tempNode = self.head 
        count  = 0 

        while tempNode:
            if tempNode.data == num:
                count += 1
            tempNode = tempNode.next

        return count


            
    


        



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(1)
node5 = Node(3
             )
node6 = Node(3)
node7 = Node(1)

ddll = DdLL()

ddll.insertionOfDll(node1)
ddll.insertionOfDll(node2)
ddll.insertionOfDll(node3)
ddll.insertionOfDll(node4)
ddll.insertionOfDll(node5)
ddll.insertionOfDll(node6)
ddll.insertionOfDll(node7)

ddll.printDll()

print("the occurance of #3 is : " , ddll.occuranceOfNumber(3))