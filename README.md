# Sistem Prediksi Asma berbasis IoT 💨

<p align="center">
  <img src="additional/logo.jpeg" alt="Logo Proyek" width="150"/>
</p>

<p align="center">
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Language-Python-blue.svg?style=flat-square" alt="Language" style="margin-right: 8px;"/>
  </a>
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Framework-TensorFlow-orange.svg?style=flat-square" alt="TensorFlow" style="margin-right: 8px;"/>
  </a>
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Framework-Keras-red.svg?style=flat-square" alt="Keras" style="margin-right: 8px;"/>
  </a>
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Framework-Flask-green.svg?style=flat-square" alt="Flask" style="margin-right: 8px;"/>
  </a>
    <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Database-MongoDB-brightgreen.svg?style=flat-square" alt="MongoDB" style="margin-right: 8px;"/>
  </a>
    <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Platform-Streamlit-blueviolet.svg?style=flat-square" alt="Streamlit" style="margin-right: 8px;"/>
  </a>
</p>

Proyek ini mengimplementasikan sistem prediksi asma berbasis IoT, memanfaatkan data sensor, model pembelajaran mesin, dan antarmuka pengguna yang intuitif. Tujuannya adalah untuk memberikan peringatan dini kepada pasien asma dan membantu mereka mengelola kondisi mereka dengan lebih efektif. Sistem ini mengintegrasikan data dari perangkat IoT, memprosesnya menggunakan model TensorFlow/Keras yang telah dilatih, dan menyajikannya melalui aplikasi web Streamlit yang mudah digunakan.

**Fitur Utama ✨**

*   **Prediksi Risiko Asma Real-time 🚨**: Memprediksi kemungkinan serangan asma berdasarkan data sensor IoT dan riwayat pasien.
*   **Aplikasi Web Interaktif 📊**: Aplikasi Streamlit yang intuitif untuk visualisasi data, prediksi, dan manajemen pasien.
*   **Integrasi IoT ☁️**: Kemampuan untuk mengumpulkan dan memproses data dari berbagai perangkat IoT.
*   **API berbasis Flask ⚙️**: Menyediakan API untuk berinteraksi dengan model pembelajaran mesin dan basis data.

**Tech Stack 🛠️**

*   Bahasa: Python 🐍
*   Framework: TensorFlow, Keras, Flask, Streamlit 
*   Basis Data: MongoDB 💾
*   IoT: Integrasi data sensor (format data sensor diasumsikan) 📡

**Instalasi & Menjalankan 🚀**

1.  Clone repositori:
    ```bash
    git clone https://github.com/EevnxyEgo/SIC-Final-Project
    ```
2.  Masuk ke direktori:
    ```bash
    cd SIC-Final-Project
    ```
3.  Install dependensi:
    ```bash
    pip install -r requirements.txt
    ```
4.  Jalankan aplikasi Streamlit:
    ```bash
    streamlit run streamlit_app.py
    ```
   Untuk menjalankan API Flask, gunakan perintah berikut:
    ```bash
    python api/api.py
    ```

**Cara Berkontribusi 🤝**

1.  Fork repositori ini.
2.  Buat branch untuk fitur atau perbaikan Anda: `git checkout -b feature/nama-fitur`
3.  Lakukan commit perubahan Anda: `git commit -m 'Tambahkan fitur baru'`
4.  Push ke branch Anda: `git push origin feature/nama-fitur`
5.  Buat Pull Request.

**Lisensi 📄**

Lisensi proyek tidak disebutkan.


---
README.md ini dihasilkan secara otomatis oleh [README.MD Generator](https://github.com/emRival) — dibuat dengan ❤️ oleh [emRival](https://github.com/emRival)
