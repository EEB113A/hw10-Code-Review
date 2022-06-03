    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        ans = 0
        a = 0
        while(key>0):                       #將keys中的數字轉為記憶體位置
            a = key % 10
            key = key // 10
            ans += a
        return ans
   
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = Node(key)                             #將key做成Node物件
        self.head = self.data[addr]                 #把鏈結串列的head設成self.data中的一個記憶體位置
        for i in range(addr):
            if self.head.next == None:
                self.head.next = tmp                #當self.head指的下個節點為None，令下個節點為碰撞的物件
                break
            else:
                self.head = self.head.next          #當self.head指的下個節點不為None，將首節點變成下個節點
        
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)                       #先將addr設為記憶體位置
        self.head = self.data[addr]                 #把鏈結串列的head設成self.data中的一個記憶體位置
        for i in range(addr):
            if self.head != None:                       #當首節點不為None執行
                if key == self.head.val:                    #當key的值符合目前首節點的值
                    return addr                             #回傳key的記憶體位置
                else:                                       #當key的值不符合目前首節點的值
                    self.head = self.head.next              #將首節點變成下個節點
        return None                                 #當全部執行完沒有找到有key值的記憶體位置，則回傳None