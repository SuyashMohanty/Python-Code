# FIFO first item we insert is the first one we take out

class Queue:
    
    def __init__(self):
        self.queue = []
        
    # O(1) running time
    def is_empty(self):
        return self.queue == []
    
    # this operation has O(1) running time
    def enqueue(self, data):
        self.queue.append(data)
        
    # O(N) linear running time, since need to remove 1st item in an array
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return print("Queue is empty")
   
    # O(1) constant running time 
    def peek(self):
        return self.queue[0]
    
    # O(1) constant running time
    def size_queue(self):
        return len(self.queue)
    
 
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print('size: ', queue.size_queue())
print("Dequeue: ", queue.dequeue())
print('size: ', queue.size_queue())
 