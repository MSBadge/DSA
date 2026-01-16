# How to create Node and SLL

class Node:
    def __init__(self,val):
        self.val= val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        if not self.head:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def insert_at(self,val,position):
        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count+=1
            prev_node.next = new_node
            new_node.next = current

    def delete_at(self,val):
        tem = self.head
        if tem.next is not None:
            if tem.val == val:
                self.head = tem.next
                return
            else:
                found = False
                prev = None
                while tem is not None:
                    if tem.val == val:
                        found = True
                        break
                    prev = tem
                    tem = tem.next
                if found:
                    prev.next = tem.next
                    return
                else:
                    print("Node not found")





sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(25)
sll.insert_at(22,2)
sll.delete_at(20)
sll.traverse()