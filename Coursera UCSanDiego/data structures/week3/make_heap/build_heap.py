# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    def _left_child(i):
      return 2 * i + 1

    def _right_child(i):
      return 2 * i + 2

    def _sift_down(i):
      # choose the minimum child node to swap
      min_index = i

      left_child_index = _left_child(i)
      if left_child_index < len(self._data) and self._data[left_child_index] < self._data[min_index]:
        min_index = left_child_index

      right_child_index = _right_child(i)
      if right_child_index < len(self._data) and self._data[right_child_index] < self._data[min_index]:
        min_index = right_child_index

      # go down
      if i != min_index:
        # record swappings
        self._swaps.append((i, min_index))
        # swap and go down further
        self._data[min_index], self._data[i] = self._data[i], self._data[min_index]
        _sift_down(min_index)

    def _build_heap(data):
      for i in range(len(data)//2 - 1, -1, -1):
        _sift_down(i)

    _build_heap(self._data)
    

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
