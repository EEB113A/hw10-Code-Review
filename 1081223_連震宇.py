    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        x = sum([int(a) for a in str(key)])  # 將key的數值一個一個拆開，並把它加總
        return x  # 回傳 x值

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        cur = self.data[addr]  # 定義第一個輸入的 Node為 cur
        while cur.next != None:  # 當讀取到下一個節點為 None時跳出迴圈
            cur = cur.next  # cur等於下一個節點的值
        cur.next = Node(key)  # cur的下一個節點的值為節點(key)

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        # ========================================================
        now = self.data[self.hash(key)]  # now為當前 self.data裡的節點位置
        while now != None:  # 如果節點為空，跳出迴圈
            if now.val == key:  # 節點值等於 key時
                return self.hash(key)  # 回傳節點的位置
            else:
                now = now.next  # 如果不是 key就往下一個節點
        return None  # 如果串列裡搜尋不到，回傳 None