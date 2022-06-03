    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        k=key
        total=0
        while k!=0:
            total = k % 10 + total    #將key取餘數得到目前個位數的數字並加上前面餘數的總和
            k=k//10                   #key=key的商
        return total                  #回傳key中全部數字的總和
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        
        cur = self.data[addr]         #將cur貼到當前位址
        while cur.next != None:       #如果cur的next已有東西存在   
            cur = cur.next            #cur貼到cur的next
        cur.next = Node(key)          #直到找到沒有存取物件的節點，在其新增一節點
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        
        addr = self.hash(key)         
        cur=self.data[addr]           #將cur貼到當前位址
        if self.data[addr] == key:    #如果這個位址的物件等於key  
            return addr               #將此位址回傳  
        else:                         #如果這個位址的物件不等於key 
            while cur!=None:          #如果cur已存在物件     
                if cur.val==key:      #如果此位址的值等於key
                    return addr       #將此位址回傳
                cur=cur.next          #cur貼到cur的next
            return None               #此key不存在 回傳None