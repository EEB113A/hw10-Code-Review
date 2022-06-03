    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        element_list = []        #拆開的key保存的list
        for ele in str(key):     #將key裡的每一項加入element_list
            element_list.append(int(ele))
        return sum(element_list) #加總element_list後回傳成為address
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        self.head = self.data[addr] #self.data為一個node
        keynode = Node(key)
        tmp = self.head
        while tmp.next:
            tmp = tmp.next          #往linked list下一個節點走訪
        tmp.next = keynode          #頭的下一個節點就是key節點
                  
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        address = self.hash(key)
        if self.data[address]:
            if self.data[address].val == key:
                return address
            else:
                cur = self.data[address]    #linked list 的開頭
                while cur is not None:
                    if cur.next is None:    #假如linked list 的下一個node是None回傳None
                        return None
                    if cur.val != key:      #假如走訪到的node不等於要搜尋的
                        cur = cur.next      #就往下一個node走
                        if cur.val == key:  #直到找到和要搜尋的key，node相同時，回傳 address
                            return address