    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        lens=len(str(key)) #算長度
        sum=0 #初始sum
        for i in range(0,lens): #迴圈處理
            sum=sum+key%10
            key=int(key/10)
        return sum #回傳
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        node =  self.data[addr] #定義node
        while node.next != None : #如果node.next不為None
            node = node.next #使node變成node的下一個節點
        node.next = Node( key ) #把key值存在node.next
        
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key) #定義addr
        node = self.data[addr] #定義node

        while node != None : #當node不為None
            if node.val == key : #如果node的值與key相等
                return addr  #回傳addr
            node = node.next #使node變成node的下一個節點
        return None #不存在就回傳None