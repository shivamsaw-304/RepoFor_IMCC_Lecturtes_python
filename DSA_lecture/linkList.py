

# code block of Creating Node and Linked List
#  creation of node block 
class Node :

    def __init__(self,value):
        self.data = value
        self.next = None

# creation of link list and implementatiion of codes of questions
class LinkList :

    def __init__(self):
        self.head = None
        


    def append(self,newNode):
        if self.head == None:
            self.head = newNode
            return 
        else:
            temp = self.head

        while temp.next :
            temp = temp.next

        temp.next = newNode



    def  printLL(self):

        temp = self.head

        while(temp != None):
            print(temp.data , end="-->")
 
            temp = temp.next
        print("none")


node1 = Node("last")
node2 = Node("shivam")
node3  = Node(21)
node4 = Node(22)

ll = LinkList()

ll.append(node4)
ll.append(node3)
ll.append(node2)
ll.append(node1)

ll.printLL()


    