"""
PRAKTIKUM DOUBLY LINKED LIST -- TIPE C   (Soal 23 s.d. 33)
=====================================================================
Data awal tipe ini : ['P', 'Q', 'R', 'S', 'T']
Catatan tipe       : List 5 node dan target berada di UJUNG list
                     (first / last harus ikut diperbarui).

CARA KERJA
- Setiap nomor soal dikerjakan oleh SATU mahasiswa. Isi NIM & NAMA pada blok
  identitas milik nomor soal Anda, lalu tulis kode pada fungsi soal Anda
  (ganti baris `pass`). Jangan mengubah nama fungsi/parameter dan helper.py.
- Jalankan  python3 soal_tipe_C.py  untuk melihat hasil pengujian otomatis.

STRUKTUR OBJEK (ada di helper.py, tinggal dipakai)
    class Node:
        self.info  -> data node (mis. "P") [atau self.isi]
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
# SOAL 23 -- Insert Empty Node
# ======================================================================
NIM_23 = "ISI_NIM"
NAMA_23 = "ISI_NAMA"

def soal_23_insert_empty(dll, data):
    """
    Sisipkan node berisi "Y" ke list yang masih KOSONG.
    Kondisi awal : KOSONG
    Hasil        : Y

    PSEUDOCODE:
    P = Node(data)
    dll.first = P
    dll.last = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 24 -- Insert First Node
# ======================================================================
NIM_24 = "ISI_NIM"
NAMA_24 = "ISI_NAMA"

def soal_24_insert_first(dll, data):
    """
    Sisipkan node "V" di posisi PALING DEPAN list.
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : V <-> P <-> Q <-> R <-> S <-> T

    PSEUDOCODE:
    P = Node(data)
    P.next = dll.first
    dll.first.prev = P
    dll.first = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 25 -- Insert Last Node
# ======================================================================
NIM_25 = "ISI_NIM"
NAMA_25 = "ISI_NAMA"

def soal_25_insert_last(dll, data):
    """
    Sisipkan node "W" di posisi PALING BELAKANG list.
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : P <-> Q <-> R <-> S <-> T <-> W

    PSEUDOCODE:
    P = Node(data)
    P.prev = dll.last
    dll.last.next = P
    dll.last = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 26 -- Insert After Target Node
# ======================================================================
NIM_26 = "ISI_NIM"
NAMA_26 = "ISI_NAMA"

def soal_26_insert_after(dll, node_target, data):
    """
    Sisipkan node "X" tepat SETELAH node_target (node "T" / dll.last).
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : P <-> Q <-> R <-> S <-> T <-> X

    PSEUDOCODE:
    P = Node(data)
    P.prev = node_target
    node_target.next = P
    dll.last = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 27 -- Insert Before Target Node
# ======================================================================
NIM_27 = "108102500038"
NAMA_27 = "Bintang Cahya Brilliant Putra"

def soal_27_insert_before(dll, node_target, data):
    """
    Sisipkan node "Z" tepat SEBELUM node_target (node "P" / dll.first).
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : Z <-> P <-> Q <-> R <-> S <-> T

    PSEUDOCODE:
    P = Node(data)
    P.next = node_target
    node_target.prev = P
    dll.first = P
    """
    P = Node(data)
    P.next = node_target
    node_target.prev = P
    dll.first = P

# ======================================================================
# SOAL 28 -- Traverse Maju
# ======================================================================
NIM_28 = "ISI_NIM"
NAMA_28 = "ISI_NAMA"

def soal_28_traverse_maju(dll):
    """
    Telusuri list dari first ke last, kembalikan string info node dipisah " <-> ".
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : "P <-> Q <-> R <-> S <-> T"

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
# SOAL 29 -- Traverse Mundur
# ======================================================================
NIM_29 = "ISI_NIM"
NAMA_29 = "ISI_NAMA"

def soal_29_traverse_mundur(dll):
    """
    Telusuri list dari last ke first, kembalikan string info node dipisah " <-> ".
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : "T <-> S <-> R <-> Q <-> P"

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
# SOAL 30 -- Search Target
# ======================================================================
NIM_30 = "ISI_NIM"
NAMA_30 = "ISI_NAMA"

def soal_30_search(dll, target):
    """
    Cari node berisi "T" dan kembalikan NODE-nya (bukan string). List tidak berubah.
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : node "T"

    PSEUDOCODE:
    P = dll.first
    WHILE P is not None:
        IF P.info == target:
            RETURN P
        P = P.next
    RETURN None
    """
    P = dll.first
    while P is not None:
        if P.info == target:
            return P
        P = P.next
    return None

# ======================================================================
# SOAL 31 -- Delete First Node
# ======================================================================
NIM_31 = "ISI_NIM"
NAMA_31 = "ISI_NAMA"

def soal_31_delete_first(dll):
    """
    Hapus node PALING DEPAN dari list.
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : Q <-> R <-> S <-> T

    PSEUDOCODE:
    dll.first = dll.first.next
    dll.first.prev = None
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 32 -- Delete Last Node
# ======================================================================
NIM_32 = "ISI_NIM"
NAMA_32 = "ISI_NAMA"

def soal_32_delete_last(dll):
    """
    Hapus node PALING BELAKANG dari list.
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : P <-> Q <-> R <-> S

    PSEUDOCODE:
    dll.last = dll.last.prev
    dll.last.next = None
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 33 -- Delete Target Node
# ======================================================================
NIM_33 = "ISI_NIM"
NAMA_33 = "ISI_NAMA"

def soal_33_delete_node(dll, node_target):
    """
    Hapus node_target (node "T" / dll.last) dari list.
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : P <-> Q <-> R <-> S

    PSEUDOCODE:
    dll.last = node_target.prev
    dll.last.next = None
    """
    pass  # <-- tulis kode Anda di sini


if __name__ == "__main__":
    jalankan_pengujian(23, "Insert Empty Node", NAMA_23, NIM_23, soal_23_insert_empty,
                       [], ('Y',), "Y", "ubah")
    jalankan_pengujian(24, "Insert First Node", NAMA_24, NIM_24, soal_24_insert_first,
                       ['P', 'Q', 'R', 'S', 'T'], ('V',), "V <-> P <-> Q <-> R <-> S <-> T", "ubah")
    jalankan_pengujian(25, "Insert Last Node", NAMA_25, NIM_25, soal_25_insert_last,
                       ['P', 'Q', 'R', 'S', 'T'], ('W',), "P <-> Q <-> R <-> S <-> T <-> W", "ubah")
    jalankan_pengujian(26, "Insert After Target Node", NAMA_26, NIM_26, soal_26_insert_after,
                       ['P', 'Q', 'R', 'S', 'T'], ('T', 'X'), "P <-> Q <-> R <-> S <-> T <-> X", "ubah")
    jalankan_pengujian(27, "Insert Before Target Node", NAMA_27, NIM_27, soal_27_insert_before,
                       ['P', 'Q', 'R', 'S', 'T'], ('P', 'Z'), "Z <-> P <-> Q <-> R <-> S <-> T", "ubah")
    jalankan_pengujian(28, "Traverse Maju", NAMA_28, NIM_28, soal_28_traverse_maju,
                       ['P', 'Q', 'R', 'S', 'T'], (), "P <-> Q <-> R <-> S <-> T", "string")
    jalankan_pengujian(29, "Traverse Mundur", NAMA_29, NIM_29, soal_29_traverse_mundur,
                       ['P', 'Q', 'R', 'S', 'T'], (), "T <-> S <-> R <-> Q <-> P", "string")
    jalankan_pengujian(30, "Search Target", NAMA_30, NIM_30, soal_30_search,
                       ['P', 'Q', 'R', 'S', 'T'], ('T',), "T", "node")
    jalankan_pengujian(31, "Delete First Node", NAMA_31, NIM_31, soal_31_delete_first,
                       ['P', 'Q', 'R', 'S', 'T'], (), "Q <-> R <-> S <-> T", "ubah")
    jalankan_pengujian(32, "Delete Last Node", NAMA_32, NIM_32, soal_32_delete_last,
                       ['P', 'Q', 'R', 'S', 'T'], (), "P <-> Q <-> R <-> S", "ubah")
    jalankan_pengujian(33, "Delete Target Node", NAMA_33, NIM_33, soal_33_delete_node,
                       ['P', 'Q', 'R', 'S', 'T'], ('T',), "P <-> Q <-> R <-> S", "ubah")