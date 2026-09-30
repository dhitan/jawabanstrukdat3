"""
PRAKTIKUM DOUBLY LINKED LIST -- TIPE B   (Soal 12 s.d. 22)
=====================================================================
Data awal tipe ini : ['K', 'L', 'M', 'N']
Catatan tipe       : List lebih panjang (4 node), target di tengah.

CARA KERJA
- Setiap nomor soal dikerjakan oleh SATU mahasiswa. Isi NIM & NAMA pada blok
  identitas milik nomor soal Anda, lalu tulis kode pada fungsi soal Anda
  (ganti baris `pass`). Jangan mengubah nama fungsi/parameter dan helper.py.
- Jalankan  python3 soal_tipe_B.py  untuk melihat hasil pengujian otomatis.

STRUKTUR OBJEK (ada di helper.py, tinggal dipakai)
    class Node:
        self.info  -> data node (mis. "K") [atau self.isi]
        self.prev  -> pointer ke node sebelumnya (None jika di ujung kiri)
        self.next  -> pointer ke node sesudahnya  (None jika di ujung kanan)

    class DoublyLinkedList:
        self.first -> pointer ke node paling depan (None jika list kosong) [atau self.head]
        self.last  -> pointer ke node paling belakang (None jika list kosong) [atau self.tail]

- Membuat node baru : P = Node("X")
- Pointer next dan prev HARUS konsisten (diperiksa otomatis dua arah).
"""

from helper import Node, DoublyLinkedList, jalankan_pengujian


# ======================================================================
# SOAL 12 -- Insert Empty Node
# ======================================================================
NIM_12 = "ISI_NIM"
NAMA_12 = "ISI_NAMA"

def soal_12_insert_empty(dll, data):
    """
    Sisipkan node berisi "T" ke list yang masih KOSONG.
    Kondisi awal : KOSONG
    Hasil        : T

    PSEUDOCODE:
    P = Node(data)
    dll.first = P
    dll.last = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 13 -- Insert First Node
# ======================================================================
NIM_13 = "ISI_NIM"
NAMA_13 = "ISI_NAMA"

def soal_13_insert_first(dll, data):
    """
    Sisipkan node "U" di posisi PALING DEPAN list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : U <-> K <-> L <-> M <-> N

    PSEUDOCODE:
    P = Node(data)
    P.next = dll.first
    dll.first.prev = P
    dll.first = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 14 -- Insert Last Node
# ======================================================================
NIM_14 = "ISI_NIM"
NAMA_14 = "ISI_NAMA"

def soal_14_insert_last(dll, data):
    """
    Sisipkan node "V" di posisi PALING BELAKANG list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> M <-> N <-> V

    PSEUDOCODE:
    P = Node(data)
    P.prev = dll.last
    dll.last.next = P
    dll.last = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 15 -- Insert After Target Node
# ======================================================================
NIM_15 = "ISI_NIM"
NAMA_15 = "ISI_NAMA"

def soal_15_insert_after(dll, node_target, data):
    """
    Sisipkan node "W" tepat SETELAH node_target (node "L").
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> W <-> M <-> N

    PSEUDOCODE:
    P = Node(data)
    Q = node_target.next
    P.prev = node_target
    P.next = Q
    node_target.next = P
    Q.prev = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 16 -- Insert Before Target Node
# ======================================================================
NIM_16 = "ISI_NIM"
NAMA_16 = "ISI_NAMA"

def soal_16_insert_before(dll, node_target, data):
    """
    Sisipkan node "Z" tepat SEBELUM node_target (node "M").
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> Z <-> M <-> N

    PSEUDOCODE:
    P = Node(data)
    Q = node_target.prev
    P.next = node_target
    P.prev = Q
    node_target.prev = P
    Q.next = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 17 -- Traverse Maju
# ======================================================================
NIM_17 = "ISI_NIM"
NAMA_17 = "ISI_NAMA"

def soal_17_traverse_maju(dll):
    """
    Telusuri list dari first ke last, kembalikan string info node dipisah " <-> ".
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : "K <-> L <-> M <-> N"

    PSEUDOCODE:
    hasil = ""
    P = dll.first
    WHILE P is not None:
        hasil = GABUNG_STRING(hasil, P.info)
        P = P.next
    RETURN hasil
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 18 -- Traverse Mundur
# ======================================================================
NIM_18 = "ISI_NIM"
NAMA_18 = "ISI_NAMA"

def soal_18_traverse_mundur(dll):
    """
    Telusuri list dari last ke first, kembalikan string info node dipisah " <-> ".
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : "N <-> M <-> L <-> K"

    PSEUDOCODE:
    hasil = ""
    P = dll.last
    WHILE P is not None:
        hasil = GABUNG_STRING(hasil, P.info)
        P = P.prev
    RETURN hasil
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 19 -- Search Target
# ======================================================================
NIM_19 = "ISI_NIM"
NAMA_19 = "ISI_NAMA"

def soal_19_search(dll, target):
    """
    Cari node berisi "M" dan kembalikan NODE-nya (bukan string). List tidak berubah.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : node "M"

    PSEUDOCODE:
    P = dll.first
    WHILE P is not None:
        IF P.info == target:
            RETURN P
        P = P.next
    RETURN None
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 20 -- Delete First Node
# ======================================================================
NIM_20 = "ISI_NIM"
NAMA_20 = "ISI_NAMA"

def soal_20_delete_first(dll):
    """
    Hapus node PALING DEPAN dari list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : L <-> M <-> N

    PSEUDOCODE:
    dll.first = dll.first.next
    dll.first.prev = None
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 21 -- Delete Last Node
# ======================================================================
NIM_21 = "ISI_NIM"
NAMA_21 = "ISI_NAMA"

def soal_21_delete_last(dll):
    """
    Hapus node PALING BELAKANG dari list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> M

    PSEUDOCODE:
    dll.last = dll.last.prev
    dll.last.next = None
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 22 -- Delete Target Node
# ======================================================================
NIM_22 = "ISI_NIM"
NAMA_22 = "ISI_NAMA"

def soal_22_delete_node(dll, node_target):
    """
    Hapus node_target (node "L") dari list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> M <-> N

    PSEUDOCODE:
    P = node_target.prev
    Q = node_target.next
    P.next = Q
    Q.prev = P
    """
    pass  # <-- tulis kode Anda di sini


if __name__ == "__main__":
    jalankan_pengujian(12, "Insert Empty Node", NAMA_12, NIM_12, soal_12_insert_empty,
                       [], ('T',), "T", "ubah")
    jalankan_pengujian(13, "Insert First Node", NAMA_13, NIM_13, soal_13_insert_first,
                       ['K', 'L', 'M', 'N'], ('U',), "U <-> K <-> L <-> M <-> N", "ubah")
    jalankan_pengujian(14, "Insert Last Node", NAMA_14, NIM_14, soal_14_insert_last,
                       ['K', 'L', 'M', 'N'], ('V',), "K <-> L <-> M <-> N <-> V", "ubah")
    jalankan_pengujian(15, "Insert After Target Node", NAMA_15, NIM_15, soal_15_insert_after,
                       ['K', 'L', 'M', 'N'], ('L', 'W'), "K <-> L <-> W <-> M <-> N", "ubah")
    jalankan_pengujian(16, "Insert Before Target Node", NAMA_16, NIM_16, soal_16_insert_before,
                       ['K', 'L', 'M', 'N'], ('M', 'Z'), "K <-> L <-> Z <-> M <-> N", "ubah")
    jalankan_pengujian(17, "Traverse Maju", NAMA_17, NIM_17, soal_17_traverse_maju,
                       ['K', 'L', 'M', 'N'], (), "K <-> L <-> M <-> N", "string")
    jalankan_pengujian(18, "Traverse Mundur", NAMA_18, NIM_18, soal_18_traverse_mundur,
                       ['K', 'L', 'M', 'N'], (), "N <-> M <-> L <-> K", "string")
    jalankan_pengujian(19, "Search Target", NAMA_19, NIM_19, soal_19_search,
                       ['K', 'L', 'M', 'N'], ('M',), "M", "node")
    jalankan_pengujian(20, "Delete First Node", NAMA_20, NIM_20, soal_20_delete_first,
                       ['K', 'L', 'M', 'N'], (), "L <-> M <-> N", "ubah")
    jalankan_pengujian(21, "Delete Last Node", NAMA_21, NIM_21, soal_21_delete_last,
                       ['K', 'L', 'M', 'N'], (), "K <-> L <-> M", "ubah")
    jalankan_pengujian(22, "Delete Target Node", NAMA_22, NIM_22, soal_22_delete_node,
                       ['K', 'L', 'M', 'N'], ('L',), "K <-> M <-> N", "ubah")
