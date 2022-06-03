    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        k1=0 #個位數
        k2=0 #十位數
        k3=0 #百位數
        k4=0 #千位數
        k5=0 #萬位數
        k6=0 #十萬位數
        k1=key%10                              #除10取餘數
        if key>=10:
            k2=(key%100)//10                   #除100取餘數再除10取floor
            if key>=100:
                k3=(key%1000)//100             #除1000取餘數再除100取floor
                if key>=1000:
                    k4=(key%10000)//1000       #除10000取餘數再除1000取floor
                    if key>=10000:
                        k5=(key%100000)//10000 #除100000取餘數再除10000取floor
                        if key==100000:
                            k6=1
        s=k1+k2+k3+k4+k5+k6                    #各數之相加總和
        return s

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        move = self.data[addr]        #地址的資料
        while move.next:              #往下找直到尾端
            move = move.next          #當前資料指派為下一個
        move.next=Node(key)           #Node物件

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)         #地址設定
        if self.data[addr] is None:   #若資料不存在
            return None               #回傳None
        else:                         #若資料存在
            return addr               #回傳地址