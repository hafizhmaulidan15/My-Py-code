# Program Python untuk didemonstrasikan
# implementasi tumpukan menggunakan linked list memakai class node

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:

	# Menginisialisasi tumpukan.
	def __init__(self):
		self.head = Node("head")
		self.size = 0

	# Representasi string dari tumpukan
	def __str__(self):
		cur = self.head.next
		out = ""
		while cur:
			out += str(cur.value) + "->"
			cur = cur.next
		return out[:-3]

	# Mendapatkan ukuran stack
	def getSize(self):
		return self.size

	# Check apabila stack kosong
	def isEmpty(self):
		return self.size == 0

	# Dapatkan angka teratas dari stack
	def peek(self):

		# Pemeriksaan penyaringan untuk melihat apakah kita dapat melihat tumpukan kosong.
		if self.isEmpty():
			raise Exception("Melihat dari stack yang kosong")
		return self.head.next.value

    # Mmasukan nilai ke dalam stack.
	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1

	# Hapus nilai dari stack dan dikembalikan.
	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value

# Perintah mejalankan kodingan
if __name__ == "__main__":
	stack = Stack()
	for i in range(0, 11):
		stack.push(i)
	print(f"Stack: {stack}")

	for _ in range(1, 6):
		remove = stack.pop()
		print(f"Pop: {remove}")
	print(f"Stack: {stack}")