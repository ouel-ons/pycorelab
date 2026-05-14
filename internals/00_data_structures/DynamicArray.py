import ctypes



class DynamicArray(object):

	def __init__(self):
		self._size = 0
		self._capacity = 1
		self._array = self._make_array(self._capacity)

	def _make_array(self, cap):
		
		return (cap * ctypes.py_object)()

	def _resize(self, new_cap):
		_new_array = self._make_array(new_cap)

		for i in range(self._size):
			_new_array[i] = self._array[i]

		self._array = _new_array
		self._capacity = new_cap

	def append(self, val):
		if self._size == self._capacity:
			self._resize(2 * self._capacity)
		self._array[self._size] = val
		self._size += 1

	def insert(self, idx, val):
		pass

	def pop(self, indx=-1):
		pass

	def remove(self, val):
		pass

	def clear(self):
		pass

	def index(self, val):
		pass

	def count(self, val):
		pass
	def extend(self, iterable):
		pass
	def reverse(self):
		pass
	def copy(self):
		pass
	def __getitem__(self, idx):
		if not idx <= self._size:
			raise IndexError(f"{idx} is out of bound")
		return self._array[idx]

	def __setitem__(self, idx, val):
		pass

	def __len__(self):
		return self._size

	def __contains__(self, val):
		if not val in self._array:			raise IndexError("sss")
		return val in self._array

	def __iter__(self):
		pass

	def __repr__(self):
		return f"{self._array}"

	def __str__(self):
		return f"{self._array}"



a = DynamicArray()

print(a)


# print(22 in a)
