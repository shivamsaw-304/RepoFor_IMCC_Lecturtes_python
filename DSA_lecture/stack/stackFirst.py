class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self,newNode):
        newNode.next = self.top
        self.top = newNode

    def pop(self):


        if self.isEmpty :
            print("stack is empty ")
            return 

        temp = self.top
        print("poped element : " , temp.data)

        self.top  = self.top.next

        temp = None




    def printStack(self):
        temp = self.top


        while temp:
            print(temp.data)
            temp = temp.next


stack = Stack()

stack.pop()
stack.push(Node(1))
stack.push(Node(2))
stack.push(Node(3))
stack.push(Node(4))
stack.push(Node(5))
stack.push(Node(6))

stack.printStack()
stack.pop()



