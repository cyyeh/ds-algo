#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  def is_binary_tree_auxiliary(key_index, min, max):
    if key_index == -1:
      return True
    elif key[key_index] < min or key[key_index] >= max:
      return False
    
    return is_binary_tree_auxiliary(left[key_index], min, key[key_index]) and \
            is_binary_tree_auxiliary(right[key_index], key[key_index], max)

  key, left, right = tree
  if len(key):
    return is_binary_tree_auxiliary(0, -pow(2, 31), pow(2, 31))
  else:
    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  key = [0 for _ in range(nodes)]
  left = [0 for _ in range(nodes)]
  right = [0 for _ in range(nodes)]
  for i in range(nodes):
    [a, b, c] = map(int, sys.stdin.readline().split())
    key[i] = a
    left[i] = b
    right[i] = c

  tree = (key, left, right)
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
