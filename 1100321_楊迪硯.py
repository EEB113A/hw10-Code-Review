    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        total = 0
        keycopy = key
        while keycopy >0:
           n = keycopy % 10
           total+=n
           keycopy //=10
        return total
        #將數值用折疊法處理，並且回傳
        
    def collision(self, addr, key):
        loc = self.data[addr]
        cmp = Node(key)
        if loc.next == None:
            loc.next = cmp
        elif loc.next.next == None:
            loc.next = cmp
        elif loc.next.next.next == None:
            loc.next = cmp
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
    
    def search(self, key):
        address = self.hash(key)
        if self.data[address] == None:
            return None
        else:
            tmp = self.data[address]
            lst = []
            while tmp:
                lst.append(tmp.val)
                tmp = tmp.next
            if key in lst:
                return address
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None