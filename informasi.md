# Panduan Praktikum Doubly Linked List (Modern 2026 Edition)

Dokumen ini berisi panduan konsep, diagram visual vektor (SVG), dan pseudocode modern bergaya **Dot-Notation (OOP)** yang intuitif dan mudah dipahami untuk **11 Operasi Dasar Doubly Linked List**.

---

## Pembagian Soal Mahasiswa (33 Soal)

Soal praktikum dibagi menjadi 3 file berdasarkan variasi dataset awal:

| Tipe File | Nomor Soal | Data Awal | Target Pembelajaran |
|---|---|---|---|
| `soal_tipe_A.py` | Soal 01 – 11 | `['A', 'B', 'C']` | Operasi dasar list 3 node |
| `soal_tipe_B.py` | Soal 12 – 22 | `['K', 'L', 'M', 'N']` | Operasi dasar list 4 node |
| `soal_tipe_C.py` | Soal 23 – 33 | `['P', 'Q', 'R', 'S', 'T']` | Operasi dasar list 5 node |

Setiap mahasiswa mengerjakan **1 nomor soal** pada file tipe masing-masing.

---

## Konsep Objek: Node & List

### 1. Struktur Satu Node (`P`)
Setiap kotak node memiliki 3 atribut:
* **`P.prev`** : Pointer ke gerbong/node sebelah kiri (`None` jika di ujung kiri).
* **`P.info`** : Nilai data di dalam node (misal `'A'`).
* **`P.next`** : Pointer ke gerbong/node sebelah kanan (`None` jika di ujung kanan).

### 2. Struktur List Keseluruhan (`dll`)
List adalah rangkaian keretanya, dikontrol oleh dua penunjuk utama:
* **`dll.first`** : Menunjuk ke node paling depan.
* **`dll.last`** : Menunjuk ke node paling belakang.

---

## 📖 Kamus Singkat: Notasi Teori vs Notasi Modern (Python)

| Notasi Buku Ajar Teori | Notasi Modern 2026 (Koding Python) | Cara Mudah Membacanya |
|---|---|---|
| `First(L)` | **`dll.first`** | Node pertama pada list |
| `Last(L)` | **`dll.last`** | Node terakhir pada list |
| `next(P)` | **`P.next`** | Pointer kanan milik node P |
| `prev(P)` | **`P.prev`** | Pointer kiri milik node P |
| `info(P)` | **`P.info`** | Data di dalam node P |
| `prev(First(L))` | **`dll.first.prev`** | Pointer kiri milik node pertama |
| `next(Last(L))` | **`dll.last.next`** | Pointer kanan milik node terakhir |

---

# 11 Operasi Dasar Doubly Linked List

## 1. Insert Empty (Sisip di List Kosong)
Menyisipkan node baru `P` ketika list belum memiliki node sama sekali (`dll.first` dan `dll.last` masih `None`).

![Insert Empty](gambar/soal_01.svg)

**Pseudocode Modern:**
```python
P = Node(data)
dll.first = P
dll.last = P
```

---

## 2. Insert First (Sisip di Posisi Paling Depan)
Menyisipkan node baru `P` di posisi paling awal, lalu memindahkan penunjuk `dll.first` ke `P`.

![Insert First](gambar/soal_02.svg)

**Pseudocode Modern:**
```python
P = Node(data)
P.next = dll.first
dll.first.prev = P
dll.first = P
```

---

## 3. Insert Last (Sisip di Posisi Paling Belakang)
Menyisipkan node baru `P` di posisi paling akhir, lalu memindahkan penunjuk `dll.last` ke `P`.

![Insert Last](gambar/soal_03.svg)

**Pseudocode Modern:**
```python
P = Node(data)
P.prev = dll.last
dll.last.next = P
dll.last = P
```

---

## 4. Insert After Node (Sisip Setelah Node Tertentu)
Menyisipkan node baru `P` tepat setelah node target, dengan bantuan pointer `Q` sebagai tetangga sebelah kanan (`node_target.next`).

![Insert After](gambar/soal_04.svg)

**Pseudocode Modern:**
```python
P = Node(data)
Q = node_target.next

P.prev = node_target
P.next = Q
node_target.next = P
Q.prev = P
```

---

## 5. Insert Before Node (Sisip Sebelum Node Tertentu)
Menyisipkan node baru `P` tepat sebelum node target, dengan bantuan pointer `Q` sebagai tetangga sebelah kiri (`node_target.prev`).

![Insert Before](gambar/soal_05.svg)

**Pseudocode Modern:**
```python
P = Node(data)
Q = node_target.prev

P.next = node_target
P.prev = Q
node_target.prev = P
Q.next = P
```

---

## 6. Traverse Maju (Penelusuran Depan ke Belakang)
Menelusuri setiap elemen dari depan ke belakang mulai dari `dll.first` via pointer `next` hingga menemukan `None`.

![Traverse Maju](gambar/soal_06.svg)

**Pseudocode Modern:**
```python
hasil = ""
P = dll.first
WHILE P is not None:
    hasil = GABUNG_STRING(hasil, P.info)
    P = P.next
RETURN hasil
```

---

## 7. Traverse Mundur (Penelusuran Belakang ke Depan)
Menelusuri setiap elemen dari belakang ke depan mulai dari `dll.last` via pointer `prev` hingga menemukan `None`.

![Traverse Mundur](gambar/soal_07.svg)

**Pseudocode Modern:**
```python
hasil = ""
P = dll.last
WHILE P is not None:
    hasil = GABUNG_STRING(hasil, P.info)
    P = P.prev
RETURN hasil
```

---

## 8. Search Node (Pencarian Nilai)
Menelusuri list dari `dll.first` menggunakan pointer penelusur `P` untuk mencari node yang nilai datanya cocok.

![Search](gambar/soal_08.svg)

**Pseudocode Modern:**
```python
P = dll.first
WHILE P is not None:
    IF P.info == target:
        RETURN P
    P = P.next
RETURN None
```

---

## 9. Delete First (Hapus Node Paling Depan)
Menghapus elemen pertama dengan memajukan `dll.first` ke elemen berikutnya, lalu memutus `dll.first.prev` menjadi `None`.

![Delete First](gambar/soal_09.svg)

**Pseudocode Modern:**
```python
P = dll.first
dll.first = dll.first.next
dll.first.prev = None
del P
```

---

## 10. Delete Last (Hapus Node Paling Belakang)
Menghapus elemen terakhir dengan memundurkan `dll.last` ke elemen sebelumnya, lalu memutus `dll.last.next` menjadi `None`.

![Delete Last](gambar/soal_10.svg)

**Pseudocode Modern:**
```python
P = dll.last
dll.last = dll.last.prev
dll.last.next = None
del P
```

---

## 11. Delete Node (Hapus Node di Tengah)
Menghapus node target dengan menghubungkan tetangga kiri (`P = node_target.prev`) langsung ke tetangga kanan (`Q = node_target.next`).

![Delete Target](gambar/soal_11.svg)

**Pseudocode Modern:**
```python
P = node_target.prev
Q = node_target.next

P.next = Q
Q.prev = P
del node_target
```

---

## Format Validasi Output Terminal

Setiap pengujian fungsi mahasiswa akan mencetak status di terminal:

```text
soal 01 Insert Empty Node (Nama NIM) hasil : D [sesuai, info: berhasil]
soal 01 Insert Empty Node (Nama NIM) hasil : None (tidak sesuai, ekspektasi: D)
soal 01 Insert Empty Node (Nama NIM) hasil : ERROR (tidak sesuai, keterangan / eror: AttributeError: ...)
```