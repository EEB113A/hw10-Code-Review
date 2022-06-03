    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        result = 0                #先建立一個初始值
        while key > 0:            #在key大於零的清況下
            result += (key % 10)  #result加上除以十後取的餘數 再更新result
            key = key // 10       #取完一餘數後除以十繼續跑回圈進行下一次取餘數
        return result             #key不大於零 結束迴圈 回傳值
        
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        ptr = self.data[addr]    #先設ptr存放地址資料
        while ptr.next != None:  #在地址資料下一個節點中有資料的情況下
            ptr=ptr.next         #ptr更新為下個節點並繼續做迴圈
        ptr.next = Node(key)     #直到下一個節點沒有東西後 將key插入Node
        
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)       #使用hash函示取址
        if not self.data[addr]:     #若此地址沒有資料
            return None             #回傳None
        else:                       #若此地址有資料
            ptr = self.data[addr]   #建立ptr存放地址資料
            while ptr != None:      #在有地址資料的情況下
                if ptr.val == key:  #若地址資料的值和key相等
                    return addr     #回傳地址位置
                ptr=ptr.next        #迴圈結束(不等於key了)更新為下一個地址資料
            return None             #回傳None