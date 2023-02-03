class node:

    def __init__(self, data):

        self.next = None
        self.data = data

class Queue:


    def __init__(self):

        self.head = None
        self.size = 0

    def Enqueue(self, data):

        temp = node(data)

        if self.head is None:
            self.head = temp
            self.size += 1

        else:

            cur = self.head 

            while cur.next is not None:

                cur = cur.next

            cur.next = temp
            self.size += 1

        
    def Dequeue(self):

        value = self.head.data
        self.head = self.head.next
        return value

    
    def isEmpty(self):

        return self.size < 0


