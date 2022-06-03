    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        self.sum=0
        while(key//10!=0): #用除法和餘數將數字一個一個抓出來
            a=key//10
            b=key%10
            key=a
            self.sum+=b #抓出後的數字相加
            
        a=key%10
        self.sum+=a
        return self.sum #回傳相加後的數
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        #now==self.data[addr]:
        now=self.data[addr] #addr的位址
        while now.next: #找鏈結串列的尾端
            now=now.next
        now.next=Node(key) #將key插到尾端去
        
        
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        random=False
        for i in range(50):  
            cur=self.data[i] #列出每個位址來找尋key是否存在
            while cur:
                if cur.val==key: #如果位址內的值和key相同就離開
                    random=True
                    break
                else:
                    cur=cur.next #與key不同就找位址內鏈結串列的下一個值
            if random: #找到key就離開
                break
        if random: #輸入的key存在
            return i #回傳key的位址
        else:
            return None    #不存在回傳None