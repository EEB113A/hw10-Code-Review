#Function to convert the input key into the corresponding number    
    def hash(self, key):
        length = 1
        addr = 0
        while key != 0:
            addr += key % (10 * length)
            key //= (10 * length)
        return addr     #Return the address as interger  
    
    
# Make the key to be inserted into a Node object and connect it to the end of the linked list    
    def collision(self, addr, key):
        temp = self.data[addr]
        while temp.next:
            temp = temp.next
        temp.next = Node(key)   #the head of the chained series

#Function to search if the key is the same with the value in that address  
    # If the input key exists, return its address (index in self.data)  
    def search(self, key):
        addr = self.hash(key)
        if not self.data[addr]:
            return None
        temp = self.data[addr]
        while temp:
            if temp.val == key:
                return addr
            temp = temp.next
        return None     # if it doesn't exist then return None