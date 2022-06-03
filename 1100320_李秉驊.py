    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        addr = 0                 #定義初始位址為0
        skey = str(key)          #把數字key轉成字串
        for i in skey:           #迴圈每次取出字串中的一個字元
            addr += int(i)       #取出來再轉成數字和初始位址做相加
        return addr              #回傳該位址

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        cur = self.data[addr]    #定義cur為鏈結串列的 head
        while cur !=None:        #迴圈當cur不等於空時進入
            if cur.next == None: #如果cur的next指標為空，則跳出迴圈。
                break
            else:                #如果cur的next指標有其他節點存在，那麼cur再繼續沿著next指標往下找。
                cur = cur.next
        nkey = Node(key)         #建立nkey為key的節點
        cur.next = nkey          #把cur的next指標指向nkey，相同位址之資料便鏈結完成。
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)    #利用hash方法得到key的位址，並放到addr。
        cur = self.data[addr]    #定義cur為鏈結串列的 head
        while cur != None:       #迴圈當cur不等於空時進入
            if cur.val == key:   #如果目前節點的值和key相等，代表key存在於雜湊表中並回傳位址。
                return addr
            else:                #如果目前節點的值和key不相等，那麼cur再繼續沿著next指標往下找
                cur = cur.next
        return None              #結束迴圈後代表key不存在於雜湊表中，回傳None。