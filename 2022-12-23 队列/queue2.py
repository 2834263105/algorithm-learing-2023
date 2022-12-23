class Queue:                    #创建一个队列类
    def __int__(self,size=100):       #构造函数，指定队列长度
        self.queue = [0 for _ in range(size)]  #创建队列的大小
        self.size = size
        self.rear = 0 #队尾指针
        self.front = 0  #队首指针

    #入队函数
    def push(self,element):
        if not self.is_filled():
            self.rear = (self.rear+1)%self.size  #队尾指针向前加1
            self.queue[self.rear] = self.element  #将新元素填入到rear指针所指的位置
        else:
            raise IndexError("Queue is filled.")

    #出队函数
    def pop(self):
        if not self.is_empt():
            self.front = (self.front+1)%self.size  #队首指针加1
            return self.queue(self.front)  #返回新的front指针所指的值
        else:
            raise IndexError("Queue is empt.")

    #判断队列是否为空
    def is_empt(self):
        return self.rear == self.front  #队首队尾指针相等则为空

    # 判断队列是否满
    def is_filled(self):
        return (self.rear+1)%self.size == self.front #队尾指针加1后对队长取模与队首指针相等

q = Queue(5)
for i in range(4):
    q.push(i)
print(q)




