    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        key_str=str(key)           #字串
        key_str_len = len(key_str)  # 長度
        sum=0
        for i in range(key_str_len):#0開始一直到結束
            sum=sum+int(key_str[i]) #分割的資料相加
            i=i+1
        return sum
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp=self.data[addr]         #第一個指標
        while tmp!=None:            #當該節點有值就繼續執行
            if tmp.next!=None:      #如果此node的下一個有值tmp就再往下跑到下一個節點   
                tmp=tmp.next
            if tmp.next==None:      #如果此node的下一個沒有值就用Node(key)取代tmp.next
                tmp.next=Node(key)
                break
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        for i in range(len(self.data)):   #0開始直到結束50
            if self.data[i] !=None:       #此有值
                tmp = self.data[i]        #tmp該值
                while tmp != None:        #當tmp有值
                    if tmp.val == key:    #檢查此值是否有跟key相等
                        return i          #相等就直接回傳
                    tmp = tmp.next
        return None                       #沒就回傳None