# Praktikum Struktur Data - Doubly Linked List

Repository ini berisi materi panduan visual vektor (SVG), pseudocode standar buku ajar Struktur Data, mesin pengujian otomatis (`helper.py`), serta 33 soal praktikum mahasiswa yang dibagi ke dalam 3 variasi dataset.

---

## 📂 Struktur Berkas

- **`informasi.md`** : Panduan lengkap 11 Operasi Dasar Doubly Linked List disertai penjelasan konsep, diagram SVG, dan pseudocode.
- **`helper.py`** : Definisi kelas `Node`, `DoublyLinkedList`, validasi pointer dua arah, dan runner pengujian otomatis.
- **`generate_svgs.py`** : Skrip generator SVG untuk visualisasi 11 operasi Doubly Linked List.
- **`soal_tipe_A.py`** : Soal 01 – 11 (Dataset 3 node: `['A', 'B', 'C']`).
- **`soal_tipe_B.py`** : Soal 12 – 22 (Dataset 4 node: `['K', 'L', 'M', 'N']`).
- **`soal_tipe_C.py`** : Soal 23 – 33 (Dataset 5 node: `['P', 'Q', 'R', 'S', 'T']`).
- **`gambar/`** : Diagram visual vektor SVG (`soal_01.svg` s.d. `soal_11.svg`).

---

## 🚀 Cara Menjalankan Pengujian

Mahasiswa cukup memilih file tipe soal masing-masing, mengisi **NIM & NAMA**, melengkapi fungsi soal, lalu menjalankan perintah:

```bash
# Untuk Tipe A (Soal 01 s.d. 11)
python3 soal_tipe_A.py

# Untuk Tipe B (Soal 12 s.d. 22)
python3 soal_tipe_B.py

# Untuk Tipe C (Soal 23 s.d. 33)
python3 soal_tipe_C.py
```

---

## 🛠️ Regenerasi Diagram SVG

Jika ingin melakukan kustomisasi atau membuat ulang diagram visual SVG:

```bash
python3 generate_svgs.py
```
