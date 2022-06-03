    def hash(self, key):
        pp = 0                                         
        while key!=0:                                     #算出每個分開後的加總(用每次除10後的餘數加總來算)
            pp = pp + key%10
            key = key//10
        return pp                                         #回傳處理過的address
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
    
    def collision(self, addr, key):
        a = self.data[addr]
        while a.next!=None:                               #尋找這一個鏈接的尾巴
            a = a.next
        a.next = Node(key)                                #放入新節點
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
    
    def search(self, key):
        add = self.hash(key)
        a = self.data[add]
        while a!= None:                                   #如果第一個有東西，判斷這一個鏈接是否有值等於key
            if a.val == key:
                return add                                #有的話return
            a = a.next
        return None                                       #沒有的話return None
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None