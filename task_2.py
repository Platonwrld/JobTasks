# первая реализация
# из минусов размер кода
# из плюсов читабельность и лаконичность кода
class CircularBuffer:

    def __init__(self, capacity):

        self.capacity = capacity 
        self.queue = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    # добавление значения в очередь
    def enqueue(self, item):

        if self.size == self.capacity:
            print('Error: Queue is full')

        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = item
            self.size = self.size + 1

    # удаление элемента(fifo)
    def deenqueue(self):
        
        if self.size == 0:
            print('Error: Queue is empty')

            return 

        else:
            tmp = self.queue[self.head]
            self.head = (self.head + 1) % self.capacity

        self.size = self.size - 1

        return tmp 

    # метод для отображения состояния
    def display(self):

        if self.size == 0:
            print('Error: Queue is empty')

        else:
            index = self.head

            for i in range(self.size):
                print(self.queue[index])
                index = (index + 1) % self.capacity
        
ex = CircularBuffer(50)

ex.enqueue(3)
ex.enqueue(2)
ex.enqueue(8)
ex.enqueue(4)
ex.deenqueue()
ex.display()


# вторая реализация 
# из плюсов это что меньше кода
# из минусов на мой взгяд это вложенный класс, который делает код менее лаконичным как в первой реализации
class RingBuffer:
    
    def __init__ (self, size_max):
        
        self.max = size_max
        self.data = []

    class Full:
       
        def append(self, x):
           
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max

        def get(self):
            
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        
        self.data.append(x)

        if len(self.data) == self.max:
            self.cur = 0
           
            self.__class__ = self.__Full

    def get(self):
       
        return self.data


if __name__ =='__main__':
    
    x = RingBuffer(5)
    x.append(1)
    x.append(2)
    x.append(3)
    x.append(4)
    