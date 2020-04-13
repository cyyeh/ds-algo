# python3

import sys, threading

class TreeHeight:
	class Tree:
		def __init__(self, index, parent_index, children):
			self._index = index
			self._parent_index = parent_index
			self._children = children

		def _append_child(self, child):
			self._children.append(child)

	def read(self):
		self.n = int(sys.stdin.readline())
		self.nodes = [TreeHeight.Tree(int(index), int(parent_index), []) for index, parent_index in enumerate(sys.stdin.readline().split())]
		self.root = ""

	def construct_tree(self):
		for node in self.nodes:
			if node._parent_index == -1:
				self.root = node
			else:
				self.nodes[node._parent_index]._append_child(node)

	def compute_height(self):
		def compute_height_auxiliary(tree, height):
			if not tree._children:
				return height
			else:
				return max([compute_height_auxiliary(child, height + 1) for child in tree._children])

		if not self.root:
			return 0
		else:
			return compute_height_auxiliary(self.root, 1)

def main():
	tree = TreeHeight()
	tree.read()
	tree.construct_tree()
	print(tree.compute_height())

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
