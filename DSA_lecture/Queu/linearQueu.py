class Node :

    def __init__(self,data):

        self.data = data
        self.next = None


class Queue :

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front == None and self.rear == None :
            return True
        else:
            return False
    

    def enQueue(self,newNode):

        if self.front == None:
            self.front = newNode
            self.rear = newNode
          
        else:
            self.rear.next = newNode
            self.rear = newNode
           

    def printQueu(self):

        copyRear = self.rear
        copyFront = self.front

        while copyFront != copyRear :
            print(copyFront.data , end="---")
            copyFront = copyFront.next



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)


querStr = Queue()


querStr.enQueue(node1)
querStr.enQueue(node2)
querStr.enQueue(node3)
querStr.enQueue(node4)
querStr.enQueue(node5)
querStr.enQueue(node4)
querStr.enQueue(node6)
querStr.enQueue(node7)
querStr.enQueue(node8)
querStr.enQueue(node9)

querStr.printQueu()

 

    