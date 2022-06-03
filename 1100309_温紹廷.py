    def hash(self, key):
        sum = 0
        while key!=0:
            sum = sum + key % 10                                              #除10 把每一位數相加
            key = key // 10
        return sum
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
    
    def collision(self, addr, key):
        num = self.data[addr]                                                 
        while num.next != None :
            num = num.next                                                    #在碰撞的 addr 內的 Node 當串列的 head
        num.next = Node(key)                                                  #插入的 key 做成 Node連接在串列的尾端
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
    
    def search(self, key):
        add = self.hash(key)                                                  # 如果輸入的 key 存在， return他的address
        key_addr =self.data[add]
        if key_addr == None:
            return None
        while key_addr != None:                                               #如果不存在 return None
            if key_addr.val == key:
                return add
            key_addr = key_addr.next

        return None