# nopCommerce Login Automation Testing

### Oleh: Rahmat Hidayat

---

## Deskripsi Proyek
Proyek ini adalah pengujian otomatisasi untuk fitur login pada aplikasi web **nopCommerce**. Pengujian dilakukan menggunakan **Selenium** dengan pendekatan **Page Object Model (POM)** untuk memastikan struktur kode yang terorganisir dan mudah dikelola.

Pengujian dirancang untuk:
- **Login dengan kredensial valid.**
- **Login dengan kredensial tidak valid.**
- **Verifikasi elemen UI pada halaman login.**

---

## Teknologi yang Digunakan
Proyek ini dikembangkan dengan menggunakan teknologi berikut:
- **Python**: Bahasa pemrograman utama.
- **Selenium**: Untuk otomatisasi browser.
- **Pytest**: Framework pengujian.
- **Pytest-HTML**: Untuk membuat laporan hasil pengujian dalam format HTML.
- **Page Object Model (POM)**: Pendekatan desain untuk memisahkan logika pengujian dari elemen halaman.

---

## Kendala yang Dihadapi
Saat menjalankan pengujian otomatisasi, terkadang muncul verifikasi **"human verification"** (seperti CAPTCHA) setelah berhasil login.  
Namun, saat login dilakukan secara manual, verifikasi ini tidak muncul.  
Akibatnya:
- Pengujian otomatis bisa gagal jika verifikasi ini muncul karena Selenium tidak dapat menangani CAPTCHA secara langsung.  

Untuk mengatasi hal ini di masa depan, perlu ada koordinasi untuk menonaktifkan CAPTCHA pada lingkungan pengujian atau mengimplementasikan solusi lain seperti penggunaan token reCAPTCHA.

---

## Cara Menjalankan Proyek
1. **Persiapan Lingkungan:**
   - Pastikan Python sudah terinstal di sistem Anda.
   - Instal pustaka yang diperlukan dengan menjalankan perintah:
     ```bash
     pip install -r requirements.txt
     ```
   - `requirements.txt` mencakup pustaka berikut:
     - `selenium`
     - `pytest`
     - `pytest-html`

2. **Konfigurasi:**
   - Perbarui file konfigurasi untuk URL login dan kredensial di `utilities/read_properties.py`.

3. **Menjalankan Pengujian:**
   - Untuk menjalankan semua pengujian:
     ```bash
     pytest
     ```
   - Untuk menghasilkan laporan HTML:
     ```bash
     pytest --html=reports/report.html
     ```

4. **Hasil Pengujian:**
   - Hasil pengujian akan tersimpan dalam file `reports/report.html`.

---

## Struktur Direktori
project_root/ │ ├── base_pages/ │ └── login_user_page.py # Kelas untuk elemen dan aksi di halaman login │ ├── utilities/ │ └── read_properties.py # File konfigurasi untuk URL dan kredensial │ ├── tests/ │ └── test_user_login.py # File pengujian │ ├── reports/ │ └── report.html # Laporan pengujian dalam format HTML │ ├── requirements.txt # Daftar pustaka yang dibutuhkan └── README.md # Dokumentasi proyek



---

## Catatan
Jika Anda menghadapi masalah saat pengujian terkait CAPTCHA, pertimbangkan solusi berikut:
1. Gunakan lingkungan pengujian tanpa CAPTCHA.
2. Implementasikan bypass CAPTCHA menggunakan API pihak ketiga jika memungkinkan.
3. Simpan cookie sesi login untuk menghindari CAPTCHA pada pengujian berikutnya.

---

Dikembangkan oleh **Rahmat Hidayat**  
Terima kasih telah menggunakan proyek ini! 😊
