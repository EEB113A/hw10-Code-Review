    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        # 定義各個變數值
        a1=0 # 個位數10^0
        a2=0 # 十位數10^1
        a3=0 # 百位數10^2
        a4=0 # 千位數10^3
        a5=0 # 萬位數10^4
        a6=0 # 十萬位數10^5
        # 判斷出各個位數是多少
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
        out=a1+a2+a3+a4+a5+a6 # 讓index=每個位數的加總=>out
        return out

    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 +
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        cur=self.data[addr] # 設首個找到的addr節點為cur (addr為self.data中的index)
        while cur.next != None: # 不斷向下一個節點走，直到鏈結尾端才停下來
            cur = cur.next
       

        cur.next=Node(key)
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key) # 讓addr為要找的東西的那個index
        if self.data[addr]==None: # 判斷，不存在的話回傳none
            return None
        else:
            return addr # 有存在的話，回傳addr之那個值