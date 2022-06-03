    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        # ================================================
        # 用字串處理的方式將每一位數拆出，並用sum進行加總
        return sum([int(str(key)[i]) for i in range(len(str(key)))])
        # ================================================
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        # ================================================
        # 讓tmp = 該addr的首節點
        tmp = self.data[addr]
        # 循序走訪直到末節點
        while tmp.next!=None:
            tmp = tmp.next
        # 將key值加入串列中
        tmp.next = Node(key)
        # ================================================
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        # ================================================
        # 將addr先存取，有利於效能
        addr = self.hash(key)
        # 讓tmp = 該addr的首節點
        tmp = self.data[addr] 
        # 循序走訪串列
        while tmp!=None:
            # 走訪途中若有節點值符合key，則代表該key存在，回傳addr
            if(tmp.val==key):
                return addr
            tmp = tmp.next
        # 若完整走訪完串列，則表示該key不存在於HashTable中
        return None