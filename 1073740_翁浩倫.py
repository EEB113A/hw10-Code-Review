    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        #此部分先定義變數並且先初始化變數
        num_0 = 0   #10的0次方==個位數
        num_1 = 0   #10的1次方==十位數
        num_2 = 0   #10的2次方==百位數
        num_3 = 0   #10的3次方==千位數
        num_4 = 0   #10的4次方==萬位數
        num_5 = 0   #10的5次方==十萬位數

        num_0 = key % 10  #此部分%10是為了找出個位數為多少
        if key >= 10:
            num_1 = (key % 100) // 10   #此部分%100是為了找出十位數為多少
            if key >= 100:
                num_2=(key % 1000) // 100   #此部分%1000是為了找出百位數為多少
                if key >= 1000:
                    num_3 = (key % 10000) // 1000   #此部分%10000是為了找出千位數為多少
                    if key >= 10000:
                        num_4 = (key % 100000) // 10000     #此部分%100000是為了找出萬位數為多少
                        if key == 100000:
                            num_5 = 1   #此部分是為了找出十萬位數
        output = num_0 + num_1 + num_2 + num_3 + num_4 + num_5     #這部分將所有num0~num5加總即為輸出
        return output
        
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        cur = self.data[addr]   #找到第一個address並且設置為cur
        while cur.next != None:     #這部分讓他繼續一直走，走到整個link尾端為止
            cur = cur.next      #將cur.next設置為新的cur
        cur.next = Node(key)

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)   #這部分先找出address包含於他的index裏
        if self.data[addr]==None:   #這部分先進行if判斷，看看他是否存在
            return None     #這邊是當他不存在就回傳None
        else:
            return addr     #相反地，如果他是存在的話，就回傳原先的address value