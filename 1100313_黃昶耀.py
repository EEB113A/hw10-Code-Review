    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        addr = 0                #地址預設0
        num = int(key)          
        while num != 0 :        #此迴圈分解num的每個數字，再一個一個加起來給地址
            addr += num % 10
            num = num // 10
        return addr             #回傳地址
        
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr]   #指派head
        while tmp.next != None: #當tmp的下一個還不等於None時
            tmp = tmp.next      #繼續往前
        tmp.next = Node(key)    #把Node(key)連到尾端
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)   #尋找地址
        tmp = self.data[addr]   #找到head
        while tmp != None:      #當tmp不等於None時
            if tmp.val == key:  #如果值等於key
                return addr     #回傳地址
            else:
                tmp = tmp.next  #若不等於則繼續往前
        return None             #都找不到就回傳None