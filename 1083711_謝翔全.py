    def hash(self, key):
        #數字每一位分割後加總
        splitkey = [int(k) for k in str(key)]
        address = sum(splitkey)
        return address
    def collision(self, addr, key):
        #和鏈結串列的原理一樣
        self.head = self.data[addr] #self.data的元素本身就是一個Node
        keynode = Node(key)
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = keynode #頭的下一個節點就是key節點

    def search(self, key):
        address = self.hash(key)
        if self.data[address]:
            if self.data[address].val == key:
                return address
            else: 
                cur = self.data[address] #linked list的頭
                while cur is not None: #開始走訪linked list
                    if cur.next is None: #如果linked list最後沒有節點，則回傳None
                        return None 
                    if cur.val != key: #如果走訪到的節點值不等於要搜尋的值，則往下一個節點走訪。若找到和要搜尋的值一樣的節點值時，回傳位址。
                        cur = cur.next
                        if cur.val == key:
                            return address