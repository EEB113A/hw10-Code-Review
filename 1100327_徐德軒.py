    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
            x=str(key)#將x轉為字串
            sum=0
            for i in x:#利用字串可迭代的特性快速的將每位數相加得到addr
                sum+=int(i)
            return sum    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        if self.data[addr]!=None:#若該addr處已經有資料存在
            cur=self.data[addr]
            while True:#找到next指向Nonek的節點後就在該節點後方插入Node(Key)
                if cur.next==None:
                    cur.next=Node(key)
                    break
                cur=cur.next#將cur指向下一個節點
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)
        if self.data[addr]!=None:#若該addr處已經有資料存在
            cur=self.data[addr]
            while True:
                if cur.val==key:#成功在hashtable內找到該資料的話
                    return addr#回傳addr
                    break
                cur=cur.next#若沒找到就將cur指向下一個節點，重複上面的操作
                if cur==None:#若找到最後一個節點還是沒有找到該資料
                    return None#回傳None，結束迴圈
                    break
        else:
            return None#該addr處並沒有資料存在也回傳None