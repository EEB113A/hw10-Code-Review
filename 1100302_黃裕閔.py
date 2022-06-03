    def hash(self, key):
        total = 0                                       #設立變數儲存各個位數的總和
        tmp = key                                       #為了不變更原本的值設立tmp變數
        while tmp > 0:                                  #建立while迴圈提出各個位數
            n = tmp %10                                 #取10的餘數即是每個位數
            total += n                                  #將每個位數加進total
            tmp //= 10                                  #將位數加進total後整除10即可刪除那個位數
        return total                                    #最後回傳total值 就是要儲存的位置
    def collision(self, addr, key):
        loca = self.data[addr]                          #找出發生碰撞的位置
        new_Node = Node(key)                            #將發生碰撞的元素建立一個新的節點
        if loca.next == None:                           #當原本在這個位置的元素後面有位置將碰撞元素放在後面
            loca.next = new_Node                        
        elif loca.next.next == None:                    #當原本在這個位置的元素後面再後面有位置將碰撞元素放在後面
            loca.next.next = new_Node
        elif loca.next.next.next == None:               #當原本在這個位置的元素後面再後面再後面有位置將碰撞元素放在後面
            loca.next.next.next = new_Node
    
    def search(self, key):
        add = self.hash(key)                            #將要搜尋的元素利用雜湊函數轉變成記憶體位置
        if self.data[add] == None:                      #當所要找的記憶體位置是空的 直接回傳None
            return 
        else:                                           #當所要找的記憶體位置不是空的
            tmp = self.data[add]                        #設立tmp函數將此記憶體位置的元素複製
            tmp_list = []                               #建立tmp_list空list儲存此記憶體位置中的所有元素
            while tmp:                                  #建立whlie迴圈將此記憶體中的元素全部放進去
                tmp_list.append(tmp.val)                
                tmp = tmp.next
            if key in tmp_list:                         #要找的元素如果在list中則回傳記憶體位置
                return add
            else:
                return
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None