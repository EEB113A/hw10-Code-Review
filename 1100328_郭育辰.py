    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        n=int(math.log10(key))+1 #計算幾位數 
        s=0
        addr=0
        for i in range(n,0,-1):
            j=int((key-s)/pow(10,i-1))
            addr+=j
            s+=j*pow(10,i-1)
        return addr           
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp=self.data[addr]
        while tmp.next:
            tmp=tmp.next
        tmp.next=Node(key)
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        flag=False
        for i in range(50):
            if self.data[i]:
                tmp=self.data[i]
                while tmp:
                    if tmp.val==key:
                        flag=True
                        break
                    else:
                        tmp=tmp.next
                if flag:
                    break
        if flag:
            return i
        else:
            return None