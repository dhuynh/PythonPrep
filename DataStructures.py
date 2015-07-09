class Stack:

	def __init__(self):
		self.items = []

		def isEmpty(self):
			return self.items == []

		def push(self, item):
			self.items.append(item)

		def pop(self):
			return self.items.pop()

		def peek(self):
			return self.items[len(self.items)-1]

		def size(self):
			return len(self.items)

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, items):
		self.items.insert(item)

	def dequeue(self, items):
		return self.items.pop()

	def size(self):
		return len(self.items)

class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def insert(self, item):
		self.data = item

	def setNext(self, newItem):
		self.next = newItem

class LinkedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		newNode = Node(item)
		newNode.setNext(self.head)
		self.head = newNode

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head

		found = False

		while current != item and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		while current != item and not found:
			if current.getData() == item
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())


class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key

def preOrder(tree):
	if tree:
		print(tree.getRootVal)
		preOrder(tree.getLeftChild())
		preOrder(tree.getRightChild())

def postOrder(tree):
	if tree:
		postOrder(tree.getLeftChild)
		postOrder(tree.getRightChild)
		print(tree.getRootVal)

def inOrder(tree):
	if tree:
		inOrder(tree.getLeftChild)
		print(tree.get)
		inOrder(tree.getRightChild)





