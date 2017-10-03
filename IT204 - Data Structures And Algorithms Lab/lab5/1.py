class BinSearchTree:
	def __init__(self, r=None):
		self.root = BinTreeNode(r)
		self.preorder = []
		self.postorder = []

	def insert(self, k, x):
		z = BinTreeNode()
		z.key = k
		z.left_child = None
		z.right_child = None
		y = x.parent
		while (x != None):
			y = x
			if (k < x.key):
				x = x.left_child
			else:
				x = x.right_child
		z.parent = y
		if (k < y.key):
			y.left_child = z
		else:
			y.right_child = z

	def search(self, k, x):
		if (x == None):
			return None
		elif (x.key == k):
			return x
		elif (k < x.key):
			return self.search(k, x.left_child)
		else:
			return self.search(k, x.right_child)

	def minimum(self, x):
		if (x == None):
			return None
		else:
			return self.minimum(x.left_child)

	def maximum(self, x):
		if (x == None):
			return None
		else:
			return self.maximum(x.right_child)

	def successor(self, x):
		if (x.right_child != None):
			return self.minimum(x.right_child)
		y = x.parent
		while (x != y.left_child) and (y != None):
			x = y
			y = y.parent
		return y

	def predecessor(self, x):
		if (x.left_child != None):
			return self.maximum(x.left_child)
		y = x.parent
		while (x != y.right_child) and (y != None):
			x = y
			y = y.parent
		return y

	def delete(self, x):
		if (x.left_child == None) and (x.right_child == None):
			if (x.parent.left_child == x):
				x.parent.left_child = None
			else:
				x.parent.right_child = None
		elif (x.left_child != None):
			x.key = x.left_child.key
			x.left_child = None
		elif (x.right_child != None):
			x.key = x.right_child.key
			x.right_child = None
		else:
			y = predecessor(x)
			x.key = y.key
			delete(y)

	def preorder_traversal(self, x):
		if x:
			self.preorder.append(x.key)
			self.preorder_traversal(x.left_child)
			self.preorder_traversal(x.right_child)

	def postorder_traversal(self, x):
		if x:
			self.postorder.insert(0, x.key)
			self.postorder_traversal(x.right_child)
			self.postorder_traversal(x.left_child)

	def printPostfix(self):
		self.postorder_traversal(self.root)
		print(self.postorder)

	def printPrefix(self):
		self.preorder_traversal(self.root)
		print(self.preorder)


class BinTreeNode:
	def __init__(self, k=None, p=None):
		self.parent = p
		self.left_child = None
		self.right_child = None
		self.key = k

def main():
	B = BinSearchTree(5)
	B.insert(3, B.root)
	B.insert(8, B.root)
	B.insert(12, B.root)
	B.insert(7, B.root)
	print(B.root.right_child.right_child.key)
	print(B.successor(B.root.right_child.left_child).key)
	print(B.successor(B.root.right_child.left_child).key)
	B.delete(B.root.right_child.right_child)
	B.insert(2, B.root)
	print(B.root.right_child.right_child == None)
	print(B.search(7, B.root).key)
	B.preorder_traversal(B.root)
	C = BinSearchTree(1)
	C.insert(2, C.root)
	C.insert(3, C.root)
	C.insert(4, C.root)
	C.insert(5, C.root)
	C.printPrefix()

if __name__ == '__main__':
	main()