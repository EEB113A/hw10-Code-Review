    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        a1=0 #個位數的值
        a2=0 #十位數的值
        a3=0 #百位數的值
        a4=0 #千位數的值
        a5=0 #萬位數的值
        a6=0 #十萬位數的值
        a1=key%10
        if key>=10:
            a2=(key%100)//10
            if key>=100:
                a3=(key%1000)//100
                if key>=1000:
                    a4=(key%10000)//1000
                    if key>=10000:
                        a5=(key%100000)//10000
                        if key==100000:
                            a6=1
        out=a1+a2+a3+a4+a5+a6#把各個位數的值加起來為要放入的index
        return out
   
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 +
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        cur=self.data[addr]#cur當作是第一個插在此地址的node
        while cur.next != None:#一直往下一個找到鏈結尾端為止
            cur = cur.next
       
        cur.next=Node(key)
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)#先找出要找的東西他會放在哪一個index
        if self.data[addr]==None:
            return None
        else:
            return addr