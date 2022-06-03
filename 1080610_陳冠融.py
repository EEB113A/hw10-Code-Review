    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        n = sum([int(num) for num in str(key)])  # 將key拆開、加總
        return n  # 回傳n

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr]  # 第一個節點=tmp
        while tmp.next != None:  # tmp的下一個節點!=None就進入迴圈
            tmp = tmp.next  # tmp=下一個節點
        tmp.next = Node(key)  # tmp的下一個節點的值=key

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        now_node = self.data[self.hash(key)]  # now_node=節點
        while now_node != None:  # 節點!=空的就進入迴圈
            if now_node.val == key:  # 節點值=key
                return self.hash(key)  # 回傳節點
            if now_node.val != key:  # 節點值!=key
                now_node = now_node.next  # 找下一個節點
        return None  # 都找完了就回傳None