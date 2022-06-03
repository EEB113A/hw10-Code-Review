    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        addr = 0
        while key > 0:     #將key的各位數相加=addr
            r = key % 10
            addr += r
            key = key // 10
        return addr

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        while self.data[addr].next:     #鏈結
            self.data[addr] = self.data[addr].next
        self.data[addr].next = Node(key)     #key做成Node物件並連接在鏈結串列的尾端
        
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)
        if self.data[addr]:     #若輸入的 key 存在，return 他的地址
            return addr
        else:
            return None