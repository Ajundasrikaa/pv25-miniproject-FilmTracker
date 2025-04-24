import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox, QSlider,
    QPushButton, QListWidget, QVBoxLayout, QHBoxLayout, QSpinBox,
    QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class FilmTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Film Tracker - F1D022108")
        self.setGeometry(200, 200, 600, 400)
        self.init_ui()

    def init_ui(self):

        title = QLabel('\U0001F3AC' + " Film Tracker App")
        title.setFont(QFont("Arial", 20))
        title.setAlignment(Qt.AlignCenter)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Masukkan judul film")

        self.genre_combo = QComboBox()
        self.genre_combo.addItems(["Action", "Drama", "Comedy", "Romance", "Horror", "Sci-Fi", "Musical"])

        self.rating_slider = QSlider(Qt.Horizontal)
        self.rating_slider.setRange(1, 10)
        self.rating_slider.setValue(5)
        self.rating_slider.valueChanged.connect(self.update_rating_display)

        self.rating_label = QLabel("Rating: 5 " + '\u2B50')
        self.rating_label.setFont(QFont("Arial", 10))

        add_btn = QPushButton("Tambah Film")
        add_btn.clicked.connect(self.add_film)
        add_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 5px;")

        delete_btn = QPushButton("Hapus Film Terpilih")
        delete_btn.clicked.connect(self.delete_film)
        delete_btn.setStyleSheet("background-color: #f44336; color: white; font-weight: bold; padding: 5px;")
        self.delete_btn = delete_btn
        self.delete_btn.setVisible(False)

        self.film_list = QListWidget()
        self.film_list.setStyleSheet("background-color: #f0f8ff;")
        self.film_list.itemSelectionChanged.connect(self.toggle_delete_button)

        nim_label = QLabel("NIM: F1D022108")
        name_label = QLabel("Nama: AJUNDASRIKA ANUGRAHANTI TS")
        nim_label.setEnabled(False)
        name_label.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(title)

        layout.addWidget(QLabel("Judul Film:"))
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("Genre:"))
        layout.addWidget(self.genre_combo)

        layout.addWidget(QLabel("Rating (geser slider):"))
        layout.addWidget(self.rating_slider)
        layout.addWidget(self.rating_label)

        layout.addWidget(add_btn)
        layout.addWidget(self.delete_btn)

        layout.addWidget(QLabel('\U0001F4CB' + " Daftar Film:"))
        layout.addWidget(self.film_list)

        layout.addWidget(name_label)
        layout.addWidget(nim_label)

        self.setLayout(layout)

    def update_rating_display(self):
        val = self.rating_slider.value()
        self.rating_label.setText(f"Rating: {val} " + '\u2B50')

    def add_film(self):
        title = self.title_input.text()
        genre = self.genre_combo.currentText()
        rating = self.rating_slider.value()

        if title.strip() == "":
            QMessageBox.warning(self, "Peringatan", "Judul film tidak boleh kosong!")
            return

        film_info = f"{title} ({genre}) " + ('\u2B50' * rating)
        self.film_list.addItem(film_info)
        QMessageBox.information(self, "Berhasil", f"Film '{title}' ditambahkan!")

        self.title_input.clear()
        self.rating_slider.setValue(5)

    def delete_film(self):
        selected_items = self.film_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Tidak Ada Pilihan", "Pilih film yang ingin dihapus dari daftar.")
            return
        for item in selected_items:
            self.film_list.takeItem(self.film_list.row(item))
        QMessageBox.information(self, "Berhasil", "Film berhasil dihapus dari daftar.")

    def toggle_delete_button(self):
        if self.film_list.selectedItems():
            self.delete_btn.setVisible(True)
        else:
            self.delete_btn.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FilmTrackerApp()
    window.show()
    sys.exit(app.exec_())