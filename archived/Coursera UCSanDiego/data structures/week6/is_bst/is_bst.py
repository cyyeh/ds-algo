#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  def in_order_traversal(key_index, result):
    if key_index == -1:
      return
    in_order_traversal(left[key_index], result)
    result.append(key[key_index])
    in_order_traversal(right[key_index], result)

  key, left, right = tree
  is_binary_search_tree = True

  if len(key):
    result_traversal = []
    in_order_traversal(0, result_traversal)

    for index in range(len(result_traversal)):
      if index + 1 < len(result_traversal) and result_traversal[index] > result_traversal[index + 1]:
        is_binary_search_tree = False
        break

  return is_binary_search_tree


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
