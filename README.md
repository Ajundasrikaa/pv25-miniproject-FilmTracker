# pv25-miniproject-FilmTracker

# 🎬 Film Tracker App - PyQt5 Mini Project

Aplikasi GUI untuk mencatat dan mengelola daftar film, dikembangkan menggunakan **PyQt5** sebagai mini project mata kuliah *Visual Programming* semester genap 2024/2025.

---

## Deskripsi Aplikasi

Film Tracker App adalah aplikasi desktop yang memungkinkan pengguna untuk mencatat film yang ingin ditonton atau telah ditonton. Pengguna dapat memasukkan judul film, memilih genre, dan memberikan rating menggunakan slider. Semua data film akan ditampilkan dalam daftar, lengkap dengan genre dan visualisasi rating menggunakan simbol bintang.

Aplikasi ini dibangun **tanpa menggunakan Qt Designer**, semua komponen GUI dibuat dan diatur secara manual menggunakan PyQt5.

---

## Fitur Aplikasi

- Input **judul film** dengan `QLineEdit`
- Pilihan **genre film** menggunakan `QComboBox`
- **Rating film** menggunakan `QSlider` (1–10)
- Label rating interaktif yang menampilkan nilai secara real-time
- **Tombol tambah film** yang menampilkan data ke `QListWidget`
- **Tombol hapus film** yang muncul hanya jika item dalam daftar dipilih
- **Notifikasi interaktif** menggunakan `QMessageBox` untuk peringatan dan informasi
- Tampilan antarmuka yang disempurnakan dengan `setStyleSheet()`
- Menampilkan **nama dan NIM** mahasiswa secara statis di bagian bawah aplikasi
- Menggunakan **Unicode emoji** (`\U0001F3AC`, `\U0001F4CB`, `\u2B50`) untuk ikon film, daftar, dan rating

---

## 🧠 Struktur Kode Utama

| Fungsi | Deskripsi |
|--------|-----------|
| `init_ui(self)` | Menyusun seluruh komponen GUI, membuat layout, dan mengatur sinyal-sinyal |
| `update_rating_display(self)` | Menampilkan nilai slider ke label rating saat digeser |
| `add_film(self)` | Menambahkan data film dari input ke daftar film |
| `delete_film(self)` | Menghapus film terpilih dari daftar |
| `toggle_delete_button(self)` | Menyembunyikan/memunculkan tombol hapus berdasarkan item yang dipilih |

### Komponen Qt yang Digunakan:
- `QWidget`, `QLabel`, `QLineEdit`, `QComboBox`, `QSlider`, `QPushButton`, `QListWidget`
- `QVBoxLayout`
- `QMessageBox`
- `QFont`, `setStyleSheet`, `Unicode`

---
