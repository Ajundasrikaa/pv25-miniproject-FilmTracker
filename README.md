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

### Berikut Tampilan Aplikasi
# ![image](https://github.com/user-attachments/assets/9953cb11-c41d-4e4f-bfb3-93f7557aed5a)

# ![image](https://github.com/user-attachments/assets/5b0907d0-252c-4428-8014-810967efdc1c)

# ![image](https://github.com/user-attachments/assets/858fb03f-6e9e-475a-982f-fe1e259233c4)

# ![image](https://github.com/user-attachments/assets/6c33cd22-ea57-42ee-a8b2-a6f8c45eb7c4)

# ![image](https://github.com/user-attachments/assets/ee093376-24e4-4e62-96b0-dc5601637d58)

# ![image](https://github.com/user-attachments/assets/8bbe1249-60ab-4bb8-ac04-dfb3015a2e98)

# ![image](https://github.com/user-attachments/assets/5ecf47ae-2ceb-4f38-a1f1-372f6c08cc5f)

# ![image](https://github.com/user-attachments/assets/add19581-2346-4c4f-beb4-c48b01d8a6b1)



