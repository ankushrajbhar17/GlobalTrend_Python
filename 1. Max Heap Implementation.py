class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def delete_max(self):
        if not self.heap:
            return None
        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return maximum

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def _sift_down(self, index):
        left, right = 2 * index + 1, 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)

heap = MaxHeap()
heap.insert(3)#insert
heap.insert(5)
heap.insert(1)
heap.insert(7)
print(heap.get_max())#max value
print(heap.delete_max())#delete max
print(heap.get_max())
