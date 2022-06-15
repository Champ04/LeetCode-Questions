class MyQueue(object):

    def __init__(self):
        self.stack1 = [] 
        self.stack2 = [] 
        

    def push(self, x):
        while not len(self.stack1) == 0:
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(x)
        while not len(self.stack2) == 0:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()
        
    def peek(self):
        return self.stack1[len(self.stack1)-1]
        
    def empty(self):
        return len(self.stack1) == 0
    
    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
