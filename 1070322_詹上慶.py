    def hash(self, key):
        # 用「摺疊法」(以1為長度)把輸入的 key 轉化為對應的數字
        # return 型態為整數 int
        # 定義各個變數值
        a1=0 # 個位數10^0
        a2=0 # 十位數10^1
        a3=0 # 百位數10^2
        a4=0 # 千位數10^3
        a5=0 # 萬位數10^4
        a6=0 # 十萬位數10^5
        # 判斷出每個位數是多少
        a1=key%10 # 個
        if key>=10:
            a2=(key%100)//10 # 十
            if key>=100:
                a3=(key%1000)//100 # 百
                if key>=1000:
                    a4=(key%10000)//1000 # 千
                    if key>=10000:
                        a5=(key%100000)//10000 # 萬
                        if key==100000:
                            a6=1 # 十萬
        out=a1+a2+a3+a4+a5+a6 # 使index=每個位數之加總=>out
        return out

    
    def collision(self, addr, key):
        # 用「鏈結法」去處理碰撞，在碰撞的 +
        # 把想插入的 key 做成為 Node 物件並且連接在鏈結串列之尾端
        # hint : addr 為 self.data 中的 index
        cur=self.data[addr] # 將首個找到的addr節點設為cur (addr為self.data中的index)
        while cur.next != None: # 不斷的往下一個節點走，直到鏈結尾端才停下來
            cur = cur.next
       

        cur.next=Node(key)
    
    def search(self, key):
        # 如果輸入的 key 存在，則 return 的地址 (在self.data中的index)
        # 如果不存在 return None
        addr = self.hash(key) # 使addr為要找的東西的那個index
        if self.data[addr]==None: # 去判斷，不存在就回傳none
            return None
        else:
            return addr # 存在的話，回傳addr的那個值