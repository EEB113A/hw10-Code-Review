    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int

        addr = sum([int(i) for i in list(str(key))])            #把key分割後相加

        return addr                                             #return 相加後的值

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index

        node = self.data[addr]                   #設定node值

        prev = node                             #設好前一個的值
        while node is not None:                 #如果前一個不是none
            prev = node                         #前一個就是node
            node = node.next                    #node就是node後一個
        prev.next = Node(key)                   #頭的下一個就是key

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None

        addr = self.hash(key)                           #先求這裡的addr
        if self.data[addr] != None:                     #若那個位子不等於None
            return addr                                 #回傳addr
        else:
            return None                                 #否則回傳None