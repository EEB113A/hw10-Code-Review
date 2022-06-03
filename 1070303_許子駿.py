    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        key_str=str(key)            #將key轉成字串
        key_str_len=len(key_str)    #計算字串key長度
        sum=0                       #設定初始sum值等於0
        for i in range(key_str_len):#從字串0的位置開始執行動作一直到字串結束
            sum=sum+int(key_str[i]) #以1為長度分割，將分割後的資料相加
            i=i+1                   #i+1  
        return sum                  #回傳sum
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp=self.data[addr]         #設定tmp為指向資料中第一個node的指標
        while tmp!=None:            #當該節點有值就繼續執行
            if tmp.next!=None:      #如果此node的下一個有值tmp就再往下跑到下一個節點   
                tmp=tmp.next
            if tmp.next==None:      #如果此node的下一個沒有值就用Node(key)取代tmp.next
                tmp.next=Node(key)
                break               #結束迴圈

    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        for i in range(len(self.data)):   #從data 0的位置開始執行動作一直到data結束(題目預設data長度為50)
            if self.data[i] !=None:       #如果此地址有值
                tmp = self.data[i]        #tmp等於該地址之值
                while tmp != None:        #當tmp有值
                    if tmp.val == key:    #檢查此值是否有跟key相等
                        return i          #相等就直接回傳
                    tmp = tmp.next
        return None                       #都沒找到就回傳None