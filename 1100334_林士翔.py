    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        
        addr=0       
        while key!=0: # 將每個位數相加
            addr+=key%10 # 取出餘數加到addr
            key  =key//10 
        return addr

            
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        
        head=self.data[addr]
        while head.next:  # 找出鏈結串列的最後一個節點
            head=head.next
        head.next=Node(key) # 將最後一個節點指向新節點
        
            
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        
        addr=self.hash(key) 
        head=self.data[addr]
        while head: # 做鏈結串列的走訪
            if head.val==key: # 如果有找到則回傳位置
                return addr
            head=head.next
        return head # 如果沒找到則回傳None