    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        
        key_s = [int(a) for a in str(key)] #str()將key轉換為字串，將字串分解為離散數字，使用int()將數字轉換回整數。
        addr = sum(key_s)                  #加總
        return addr                        #回傳地址位置
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index

        cur = self.data[addr]      #在該位置的head
        while cur.next:            # 將key插入鏈結串列尾端
            cur = cur.next
        cur.next = Node(key)
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None

        addr = self.hash(key)      #key的位置 
        cur = self.data[addr]      #在該位置的head
        while cur != None:         #如果存在回傳地址
            if cur.val == key:     #如果節點值等於key
                return addr        
            else:                  #如果不等於，再往下一個節點
                cur = cur.next     
                return addr        
        else:                      
            return None            #不存在回傳None