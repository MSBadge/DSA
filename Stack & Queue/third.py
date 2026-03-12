# valid paramthesis (leetcode 20)
class Mystack:
    def __init__(self):
        self.arr = []
        self.map = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

    def check(self, data):
        for i in range(len(data)):
            if data[i] in self.map.keys():
                self.arr.append(data[i])

            else:
                ch = self.arr.pop()
                if ch == self.map.


stack = Mystack()
a = stack.check("{[()}")
print(a)
print(stack.arr)