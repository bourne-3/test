class Fibonacci(object):  # 通过迭代器来实现，什么时候需要就什么时候调用，不会浪费空间
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0  # 之所以要把a和b放在init里面，就是要让其在基础上操作
        self.b = 1

    def __iter__(self):
        """如果想要一个对象成为一个可以迭代的对象，则可以使用for来实现__iter__方法"""
        return self  # __iter__方法的返回值是一个迭代器

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopAsyncIteration  # for循环自动停止了


fibo = Fibonacci(10)

for num in fibo:  # next的方法内有什么，就给name什么
    print(num)
