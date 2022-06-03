    def hash(self, key):
        a1=0                                       #令個位數
        a2=0                                       #令十位數
        a3=0                                       #令百位數
        a4=0                                       #令千位數
        a5=0                                       #令萬位數
        a6=0                                       #令十萬位數
        a1=key%10                                  #取個位數
        if key>=10:                                #若key大於十
            a2=(key%100)//10                       #取十位數
            if key>=100:                           #若key大於百
                a3=(key%1000)//100                 #取百位數
                if key>=1000:                      #若key大於千
                    a4=(key%10000)//1000           #取千位數
                    if key>=10000:                 #若key大於萬
                        a5=(key%100000)//10000     #取萬位數
                        if key==100000:            #若key等於十萬
                            a6=1                   #取十萬位數
        out=a1+a2+a3+a4+a5+a6                      #累加到要放入的index
        return out                                 #回傳

    
    def collision(self, addr, key):
        cur=self.data[addr]           #令cur為第一個node
        while cur.next != None:       #一直往next找，直到空
            cur = cur.next            #cur的下一個取代cur
        cur.next=Node(key)            #cur的下一個為node
    
    def search(self, key):
        addr = self.hash(key)            #先找出要找的東西他會放在哪一個index
        if self.data[addr]==None:        #若為空
            return None                  #回傳none
        else:                            #若非空
            return addr                  #回傳addr