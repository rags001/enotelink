# to create a link list node with pointers next and previous
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class linklist:
    def __init__(self, first, sec, length):
        self.first = Node(first)
        self.sec = Node(sec, prev=self.first)
        self.first.next = self.sec
        # to call a sequence of 100 fibonacci numbers
        self.fiblist(length)
        # to call a link list of reverse of 100 numbers 
        last=self.genreverse(self.first)
        # call to print the link list 
        self.printList(last)

# to create a sequence of 100 fibonacci numbers
    def fiblist(self, terms):
        current = self.sec
        for i in range(terms - 1):
            new = Node(current.data + current.prev.data, prev=current)
            current.next = new
            current = new

#to print the link list 
    def printList(self,first):
        temp=first
        while(temp): 
            print(temp.data), 
            temp = temp.next

# to revese a link list 
    def genreverse(self,head):
        current = head
        prev = None
        while current:
            tmp = current.next
            current.next = prev  
            prev = current        
            current = tmp             
        head = prev
        return head.prev

start =0
sec= 1
terms= 100
link_lst = linklist(first, sec,terms)
