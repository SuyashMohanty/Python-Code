"""
Finding Middle node ina linked list overview without using extra memory
"""

class Node:
    
    def __init__(self, data):
       self.data = data
       self.nextNode = None
       
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.numOfNodes = 0
        
    # (N/2) or O(N) linear running time complexity
    def get_middle_node(self):
        
        fast_pointer = self.head
        slow_pointer = self.head 
        
        while fast_pointer.nextNode != None and fast_pointer.nextNode.nextNode != None:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode
            
        return slow_pointer
            
    # this has O(1) running time complexity
    def insert_start(self, data):
        
        self.numOfNodes = self.numOfNodes +1
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
    
    #linear running time O(N)
    def insert_end(self, data):
        
        self.numOfNodes = self.numOfNodes +1
        new_node = Node(data)
        
        actual_node = self.head
        
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
            
        actual_node.nextNode = new_node
        
    def remove(self, data):
        
        if self.head is None:
            return
        
        self.numOfNodes = self.numOfNodes -1
        
        actual_node = self.head
        previous_node = None
        
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode
        
        # search miss - the item is not present in the linked list
        if actual_node is None:
            return
        
        if previous_node is None: # in case removing the 1st node
            self.head = actual_node.nextNode
        else: # in case of removing the specific node
            previous_node.nextNode = actual_node.nextNode
        
    #O(1)
    def size_of_linkedlist(self):
        return self.numOfNodes
    
    #O(N)
    def traverse(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode
            
            
linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(10)
print("size: ", linked_list.size_of_linkedlist())
linked_list.traverse()
print("Middle Node: ",linked_list.get_middle_node().data)
print("----------------------")
linked_list.remove(4)
print("size: ", linked_list.size_of_linkedlist())
linked_list.traverse()
          
print("Middle Node: ",linked_list.get_middle_node().data)
            