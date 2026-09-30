"""
PRAKTIKUM DOUBLY LINKED LIST -- TIPE C   (Soal 23 s.d. 33)
=====================================================================
Data awal tipe ini : ['P', 'Q', 'R', 'S', 'T']
Catatan tipe       : List 5 node dan target berada di UJUNG list
                     (First/Last harus ikut diperbarui).

CARA KERJA
- Setiap nomor soal dikerjakan oleh SATU mahasiswa. Isi NIM & NAMA pada blok
  identitas milik nomor soal Anda, lalu tulis kode pada fungsi soal Anda
  (ganti baris `pass`). Jangan mengubah nama fungsi/parameter dan helper.py.
- Jalankan  python3 soal_tipe_C.py  untuk melihat hasil pengujian otomatis.

STRUKTUR KELAS (ada di helper.py, tinggal di-import)
    class Node:
        self.info  -> data node (satu huruf, mis. "P") [kompatibel juga: self.isi]
        self.prev  -> node sebelumnya (None jika tidak ada / nil)
        self.next  -> node sesudahnya (None jika tidak ada / nil)

    class DoublyLinkedList:
        self.first -> node pertama (First(L), None jika list kosong) [kompatibel: self.head]
        self.last  -> node terakhir (Last(L), None jika list kosong)  [kompatibel: self.tail]

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
    P <- BIKIN_NODE(data)
    First(L) <- P
    Last(L) <- P
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
    P <- BIKIN_NODE(data)
    next(P) <- First(L)
    prev(First(L)) <- P
    First(L) <- P
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
    P <- BIKIN_NODE(data)
    prev(P) <- Last(L)
    next(Last(L)) <- P
    Last(L) <- P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 26 -- Insert After Target Node
# ======================================================================
NIM_26 = "ISI_NIM"
NAMA_26 = "ISI_NAMA"

def soal_26_insert_after(dll, node_target, data):
    """
    Sisipkan node "X" tepat SETELAH node_target (node "T" / Last(L)).
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : P <-> Q <-> R <-> S <-> T <-> X

    PSEUDOCODE:
    P <- BIKIN_NODE(data)
    prev(P) <- node_target
    next(node_target) <- P
    Last(L) <- P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 27 -- Insert Before Target Node
# ======================================================================
NIM_27 = "ISI_NIM"
NAMA_27 = "ISI_NAMA"

def soal_27_insert_before(dll, node_target, data):
    """
    Sisipkan node "Z" tepat SEBELUM node_target (node "P" / First(L)).
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : Z <-> P <-> Q <-> R <-> S <-> T

    PSEUDOCODE:
    P <- BIKIN_NODE(data)
    next(P) <- node_target
    prev(node_target) <- P
    First(L) <- P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 28 -- Traverse Maju
# ======================================================================
NIM_28 = "ISI_NIM"
NAMA_28 = "ISI_NAMA"

def soal_28_traverse_maju(dll):
    """
    Telusuri list dari First(L) ke Last(L), kembalikan string info node dipisah " <-> ".
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : "P <-> Q <-> R <-> S <-> T"

    PSEUDOCODE:
    hasil <- ""
    P <- First(L)
    WHILE P != NULL DO
        hasil <- GABUNG_STRING(hasil, info(P))
        P <- next(P)
    ENDWHILE
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
    Telusuri list dari Last(L) ke First(L), kembalikan string info node dipisah " <-> ".
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : "T <-> S <-> R <-> Q <-> P"

    PSEUDOCODE:
    hasil <- ""
    P <- Last(L)
    WHILE P != NULL DO
        hasil <- GABUNG_STRING(hasil, info(P))
        P <- prev(P)
    ENDWHILE
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
    P <- First(L)
    WHILE P != NULL DO
        IF info(P) == target THEN
            RETURN P
        ENDIF
        P <- next(P)
    ENDWHILE
    RETURN NULL
    """
    pass  # <-- tulis kode Anda di sini

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
    P <- First(L)
    First(L) <- next(First(L))
    prev(First(L)) <- NULL
    HAPUS_NODE(P)
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
    P <- Last(L)
    Last(L) <- prev(Last(L))
    next(Last(L)) <- NULL
    HAPUS_NODE(P)
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 33 -- Delete Target Node
# ======================================================================
NIM_33 = "ISI_NIM"
NAMA_33 = "ISI_NAMA"

def soal_33_delete_node(dll, node_target):
    """
    Hapus node_target (node "T" / Last(L)) dari list.
    Kondisi awal : P <-> Q <-> R <-> S <-> T
    Hasil        : P <-> Q <-> R <-> S

    PSEUDOCODE:
    P <- prev(node_target)
    Last(L) <- P
    next(Last(L)) <- NULL
    HAPUS_NODE(node_target)
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