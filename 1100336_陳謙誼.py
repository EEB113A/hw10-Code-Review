    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        change_key=0  #先設一個改變後的key為0以便之後累加
        while (key>0):  #當key除10取整數仍大於0時
            change_key+=key%10  #改變後的key加該key的最後一個數
            key=key//10   #把key除10取整數

        return change_key  #回傳改變後的key

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        
        self.head=self.data[addr]
        while self.head.next:
            self.head=self.head.next
        self.head.next=Node(key) #把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端

    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None

        addr=self.hash(key)  #地址設為該hash後的地址
        if key in keys:  #如果key存在
            return addr  #回傳地址
        else:  #沒有
            return None  #回傳None