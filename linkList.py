
class Node:

    def __init__(self, Data):
        self.next = None
        self.Data = Data



class LinkList:

    def __init__(self):
        self.head = None

    def add(self,Data):

        temp = Node(Data)

        if self.head is None:

            self.head = temp
        
        else:

            Current = self.head

            while Current.next != None:

                Current = Current.next

            Current.next = temp

    def pop(self):

        cur = self.head

        while cur.next is None:
            cur =cur.next

        value = cur
        cur = cur.next
        return value

        
        


    def remove(self, Data):




        Current = self.head
        
        if Current.Data == Data:
            self.head = Current.next
            return

        while Current.next is not None:

            if Current.next.Data == Data:
                break

            Current = Current.next
        
        if Current.next == None:
            print("not found")

        else: Current.next = Current.next.next


    def remove_by(self, Data):

        Cur = self.head

        if Cur.Data == Data:
            self.head = Cur.next

        while Cur != None:

            if Cur.Data == Data:
                break

            prev = Cur
            Cur = Cur.next


        if Cur == None:
                return

        else:
            Cur = prev.next
            return
       


        
    def printList(self):

        current = self.head

        while current != None:

            print(current.Data)

            current = current.next

list = LinkList()

list.add(1)
list.add(2)
list.add(3)

list.printList()

print("    ----     ")

list.pop()

list.printList()