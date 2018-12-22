# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for _ in range(self.n)]
    self.left = [0 for _ in range(self.n)]
    self.right = [0 for _ in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    def in_order_auxiliary(key_index, result):
      if key_index == -1:
        return
      in_order_auxiliary(self.left[key_index], result)
      result.append(self.key[key_index])
      in_order_auxiliary(self.right[key_index], result)

    self.result = []
    in_order_auxiliary(0, self.result)

    return self.result

  def preOrder(self):
    def pre_order_auxiliary(key_index, result):
      if key_index == -1:
        return
      result.append(self.key[key_index])
      pre_order_auxiliary(self.left[key_index], result)
      pre_order_auxiliary(self.right[key_index], result)

    self.result = []
    pre_order_auxiliary(0, self.result)
                
    return self.result

  def postOrder(self):
    def post_order_auxiliary(key_index, result):
      if key_index == -1:
        return
      post_order_auxiliary(self.left[key_index], result)
      post_order_auxiliary(self.right[key_index], result)
      result.append(self.key[key_index])

    self.result = []
    post_order_auxiliary(0, self.result)
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
