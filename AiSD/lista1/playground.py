import sys

# A min heap node
class MinHeapNode:
	def __init__(self, element, i, j):
		self.element = element
		self.i = i
		self.j = j


# A class for Min Heap
class MinHeap:
	def __init__(self, a, size):
		self.heap_size = size
		self.harr = a # store address of array
		i = (self.heap_size - 1) // 2
		while i >= 0:
			self.MinHeapify(i)
			i -= 1

	def MinHeapify(self, i):
		l = self.left(i)
		r = self.right(i)
		smallest = i

		if l < self.heap_size and self.harr[l].element < self.harr[i].element:
			smallest = l

		if r < self.heap_size and self.harr[r].element < self.harr[smallest].element:
			smallest = r

		if smallest != i:
			self.swap(i, smallest)
			self.MinHeapify(smallest)

	def left(self, i):
		return 2 * i + 1

	def right(self, i):
		return 2 * i + 2

	def getMin(self):
		return self.harr[0]

	def replaceMin(self, x):
		self.harr[0] = x
		self.MinHeapify(0)

	def swap(self, i, j):
		self.harr[i], self.harr[j] = self.harr[j], self.harr[i]


def findSmallestRange(arr, K):

	range_val = sys.maxsize
	min_val = sys.maxsize
	max_val = -sys.maxsize
	start, end = 0, 0

	harr = [MinHeapNode(0, i, 1) for i in range(K)]
	for i in range(K):
		harr[i].element = arr[i][0]
		if harr[i].element > max_val:
			max_val = harr[i].element

	hp = MinHeap(harr, K)

	while True:
		root = hp.getMin()

		min_val = root.element

		if range_val > max_val - min_val + 1:
			range_val = max_val - min_val + 1
			start = min_val
			end = max_val

		if root.j < N:
			root.element = arr[root.i][root.j]
			root.j += 1

			if root.element > max_val:
				max_val = root.element
		else:
			break

		print(max_val, min_val)

		hp.replaceMin(root)

	print("The smallest range is [{} {}]".format(start, end))


# Driver's code
if __name__ == "__main__":
	# arr = [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
    arr = [[1,2,3,1000], [0,2,2,40], [15,16,18, 41,42]]
    K = len(arr)
    N = len(arr[0])
    findSmallestRange(arr, K)
