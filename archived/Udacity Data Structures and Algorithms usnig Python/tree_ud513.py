def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def bfs(t):
	queue = []
	for tree in t:
		print(label(tree))
		queue += branches(tree)
		
	if len(queue) > 0:
		bfs(queue)
	
def dfs_pre_order(t):
	print(label(t))
	
	for b in branches(t):
		dfs_pre_order(b)

def dfs_in_order(t):
	if is_leaf(t):
		print(label(t))
		return
		
	for b in branches(t):
		dfs_in_order(b)
		if is_leaf(b):
			print(label(t))

def dfs_post_order(t):
	if is_leaf(t):
		print(label(t))
		return
		
	for b in branches(t):
		dfs_post_order(b)
	print(label(t))

t = tree('D', [tree('B', [tree('A'), tree('C')]), tree('E', [tree('F')])])

print("Tree hierarchy:")
print_tree(t)
print("Tree traversal: Breadth First Search")
bfs(t)
print("Tree traversal: Depth First Search")
print("preorder")
dfs_pre_order(t)
print("inorder")
dfs_in_order(t)
print("postorder")
dfs_post_order(t)
