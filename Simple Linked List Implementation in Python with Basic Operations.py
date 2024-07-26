class Node:  # Membuat sebuah class yang bernama Node
    def __init__(self, x):  # Menambahkan fungsi __init__ untuk membuat sebuah node yang memiliki parameter self dan x
        self.data = x  # Menginisialisasi data node dengan nilai x
        self.next = None  # Menginisialisasi pointer next dengan None

class LinkedList:  # Membuat class baru bernama LinkedList
    def __init__(self):  # Menambahkan fungsi __init__ untuk membuat sebuah linked list
        self.head = None  # Inisialisasi head dengan None
        self.tail = None  # Inisialisasi tail dengan None

    def tambah_depan(self, y):  # Membuat fungsi bernama tambah_depan yang memiliki parameter y
        node_baru = Node(y)  # Membuat node baru dengan nilai y
        if self.head is None:  # Jika linked list masih kosong
            self.head = node_baru  # Set head menjadi node baru
            self.tail = node_baru  # Set tail menjadi node baru
        else:  # Jika linked list tidak kosong
            node_baru.next = self.head  # Set next dari node baru ke head
            self.head = node_baru  # Set head menjadi node baru

    def tambah_belakang(self, y):  # Membuat fungsi tambah_belakang yang memiliki parameter y
        node_baru = Node(y)  # Membuat node baru dengan nilai y
        if self.head is None:  # Jika linked list masih kosong
            self.head = node_baru  # Set head menjadi node baru
            self.tail = node_baru  # Set tail menjadi node baru
        else:  # Jika linked list tidak kosong
            self.tail.next = node_baru  # Set next dari tail ke node baru
            self.tail = node_baru  # Set tail menjadi node baru

    def informasi_linked_list(self):  # Membuat fungsi informasi_linked_list untuk melihat informasi pada linked list
        if self.head is not None:  # Jika linked list tidak kosong
            print("Head:", self.head.data)  # Cetak data head
            print("Tail:", self.tail.data)  # Cetak data tail
        else:  # Jika linked list kosong
            print("Linked list masih kosong")

    def print_linked_list(self):  # Membuat fungsi print_linked_list untuk mencetak seluruh node pada linked list
        posisi = self.head  # Mulai dari head
        if posisi is None:  # Jika linked list kosong
            print("Linked list masih kosong")
            return
        while posisi is not None:  # Selama masih ada node
            print("[", posisi.data, "]--->", sep="", end="")  # Cetak data node
            posisi = posisi.next  # Pindah ke node berikutnya
        print("Selesai")

    def panjang(self):  # Membuat fungsi panjang untuk menghitung panjang linked list
        posisi = self.head  # Mulai dari head
        if posisi is None:  # Jika linked list kosong
            return 0
        else:
            jn = 0  # Inisialisasi jumlah node dengan 0
            while posisi is not None:  # Selama masih ada node
                jn += 1  # Tambah jumlah node
                posisi = posisi.next  # Pindah ke node berikutnya
            return jn  # Kembalikan jumlah node

    def hapus_depan(self):  # Membuat fungsi hapus_depan untuk menghapus node di depan
        if self.head is None:  # Jika linked list kosong
            print("Linked list masih kosong, tidak ada node untuk dihapus.")
            return
        target = self.head  # Node yang akan dihapus
        self.head = self.head.next  # Pindah head ke node berikutnya
        if self.head is None:  # Jika hanya ada satu node
            self.tail = None  # Set tail menjadi None
        del target  # Hapus node lama

    def hapus_node(self, x):  # Membuat fungsi hapus_node untuk menghapus node dengan nilai x
        sementara = self.head  # Mulai dari head
        if sementara is not None:
            if sementara.data == x:  # Jika node pertama adalah yang akan dihapus
                self.head = sementara.next  # Pindah head ke node berikutnya
                sementara = None  # Hapus node lama
                if self.head is None:  # Jika hanya ada satu node
                    self.tail = None  # Set tail menjadi None
                return

        while sementara is not None:
            if sementara.data == x:  # Jika ditemukan node yang akan dihapus
                break  # Keluar dari loop
            sebelumnya = sementara  # Pindah ke node berikutnya
            sementara = sementara.next

        if sementara is None:  # Jika node tidak ditemukan
            return

        sebelumnya.next = sementara.next  # Hapus node dari linked list
        if sementara == self.tail:  # Jika node yang dihapus adalah tail
            self.tail = sebelumnya  # Pindah tail ke node sebelumnya
        del sementara  # Hapus node

# Contoh penggunaan
L1 = LinkedList()
print("BANYAKNYA NODE PADA L1 adalah sebesar :", L1.panjang())
L1.tambah_depan("Jeruk")
L1.tambah_depan("Anggur")
L1.tambah_depan("Durian")
L1.informasi_linked_list()
L1.print_linked_list()
print("BANYAKNYA NODE PADA L1 adalah sebesar :", L1.panjang())
L1.tambah_belakang("Markisa")
L1.print_linked_list()
L1.informasi_linked_list()
print("BANYAKNYA NODE PADA L1 adalah sebesar :", L1.panjang())
L1.hapus_node("Anggur")
L1.print_linked_list()