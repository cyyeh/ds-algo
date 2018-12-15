#python3
import sys

# reference: https://stackoverflow.com/questions/3435926/insert-delete-max-in-o1/25468684#25468684

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = -1

    def Push(self, a):
        if len(self.__stack) == 0:
            self.__max = a
            self.__stack.append(a)
        elif a < self.__max:
            self.__stack.append(a)
        else:
            self.__stack.append(a + self.__max)
            self.__max = a
                
    def Pop(self):
        assert(len(self.__stack))
        p = self.__stack.pop()
        if abs(p) < abs(self.__max):
            return p
        else:
            self.__max = p - self.__max
            return self.__max

    def Max(self):
        assert(len(self.__stack))
        return self.__max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
