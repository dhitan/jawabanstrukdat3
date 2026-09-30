"""
helper.py -- Mesin penguji praktikum Doubly Linked List.
JANGAN DIUBAH oleh mahasiswa.
"""

import inspect


class Node:
    """Satu simpul (node) pada Doubly Linked List."""

    def __init__(self, info):
        self.info = info    # data node (satu huruf, mis. "A")
        self.prev = None    # menunjuk node sebelumnya (None = KOSONG)
        self.next = None    # menunjuk node sesudahnya (None = KOSONG)

    @property
    def isi(self):
        return self.info

    @isi.setter
    def isi(self, val):
        self.info = val


class PointerIntegrityError(Exception):
    """Dilempar bila pointer next/prev tidak simetris atau First/Last salah."""


class DoublyLinkedList:
    def __init__(self):
        self.first = None   # node pertama (First(L))
        self.last = None    # node terakhir (Last(L))

    @property
    def head(self):
        return self.first

    @head.setter
    def head(self, val):
        self.first = val

    @property
    def tail(self):
        return self.last

    @tail.setter
    def tail(self, val):
        self.last = val

    @classmethod
    def dari_list(cls, data):
        """Bangun DLL yang pointer-nya benar dari list Python (untuk data awal soal)."""
        dll = cls()
        for d in data:
            n = Node(d)
            if dll.first is None:
                dll.first = dll.last = n
            else:
                n.prev = dll.last
                dll.last.next = n
                dll.last = n
        return dll

    def ke_string(self):
        """Validasi pointer dua arah, lalu kembalikan 'A <-> B <-> C' (atau 'KOSONG')."""
        maju = validasi_pointer(self)
        return " <-> ".join(maju) if maju else "KOSONG"


def validasi_pointer(dll):
    """Periksa simetri next/prev, First(L).prev, Last(L).next, dan Last(L). Mengembalikan list info (maju)."""
    if dll.first is not None and dll.first.prev is not None:
        raise PointerIntegrityError("First(L).prev harus None")

    # --- penelusuran maju (via next) ---
    maju, ada, prev, cur = [], set(), None, dll.first
    while cur is not None:
        if id(cur) in ada:
            raise PointerIntegrityError("terdeteksi siklus pada pointer next")
        ada.add(id(cur))
        if cur.prev is not prev:
            raise PointerIntegrityError(
                f"prev pada node '{cur.info}' tidak menunjuk ke node sebelumnya")
        maju.append(cur.info)
        prev, cur = cur, cur.next
    if dll.last is not prev:
        raise PointerIntegrityError("Last(L) tidak menunjuk ke node terakhir")

    # --- penelusuran mundur (via prev) ---
    mundur, ada, nxt, cur = [], set(), None, dll.last
    while cur is not None:
        if id(cur) in ada:
            raise PointerIntegrityError("terdeteksi siklus pada pointer prev")
        ada.add(id(cur))
        if cur.next is not nxt:
            raise PointerIntegrityError(
                f"next pada node '{cur.info}' tidak menunjuk ke node sesudahnya")
        mundur.append(cur.info)
        nxt, cur = cur, cur.prev
    if mundur != maju[::-1]:
        raise PointerIntegrityError("urutan maju dan mundur tidak simetris")
    return maju


def _cari_node(dll, nilai):
    """Cari node dalam DLL berdasarkan nilainya."""
    cur = dll.first
    while cur is not None:
        if cur.info == nilai:
            return cur
        cur = cur.next
    return None


def _node_milik_list(dll, node):
    cur = dll.first
    while cur is not None:
        if cur is node:
            return True
        cur = cur.next
    return False


def jalankan_pengujian(no, nama_soal, nama, nim, fungsi, data_awal, argumen, ekspektasi, mode):
    """
    no          : nomor soal (int)
    nama_soal   : judul soal
    nama, nim   : identitas mahasiswa pemilik soal
    fungsi      : fungsi jawaban mahasiswa, dipanggil sebagai fungsi(dll, *argumen)
    data_awal   : list isi awal DLL, mis. ["A", "B", "C"] ([] = list kosong)
    argumen     : tuple argumen tambahan untuk fungsi
    ekspektasi  : kunci jawaban (string)
    mode        : "ubah"   -> DLL diubah; hasil = isi DLL sesudahnya
                  "string" -> fungsi me-return string
                  "node"   -> fungsi me-return Node; hasil = isi node tsb
    Mengembalikan True bila sesuai.
    """
    awalan = f"soal {no:02d} {nama_soal} ({nama} {nim}) hasil : "
    dll = DoublyLinkedList.dari_list(data_awal)
    try:
        # Jika parameter kedua fungsi adalah node_target / target_node, ubah argumen string pertama menjadi objek Node
        args_diteruskan = list(argumen)
        sig = inspect.signature(fungsi)
        params = list(sig.parameters.keys())
        if len(params) > 1 and params[1] in ("node_target", "target_node") and len(args_diteruskan) > 0:
            target_val = args_diteruskan[0]
            if isinstance(target_val, str):
                node_obj = _cari_node(dll, target_val)
                args_diteruskan[0] = node_obj

        hasil = fungsi(dll, *args_diteruskan)
        if mode == "ubah":
            output = dll.ke_string()
        else:
            validasi_pointer(dll)  # list tidak boleh rusak oleh penelusuran/pencarian
            if mode == "string":
                output = "None" if hasil is None else str(hasil)
            elif mode == "node":
                if hasil is None:
                    output = "None"
                elif not isinstance(hasil, Node):
                    output = f"{hasil!r} (bukan Node)"
                elif not _node_milik_list(dll, hasil):
                    output = f"{hasil.info} (bukan node milik list)"
                else:
                    output = str(hasil.info)
            else:
                raise ValueError(f"mode tidak dikenal: {mode}")
    except Exception as e:
        print(awalan + f"ERROR (tidak sesuai, keterangan / eror: {type(e).__name__}: {e})")
        return False

    if output == ekspektasi:
        print(awalan + f"{output} [sesuai, info: berhasil]")
        return True
    print(awalan + f"{output} (tidak sesuai, ekspektasi: {ekspektasi})")
    return False