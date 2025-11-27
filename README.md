# 🤖 AI Summarizer: Asisten Peringkas Dokumen Cerdas

## Deskripsi Proyek
Proyek ini adalah demonstrasi aplikasi Full Stack AI sederhana untuk meringkas teks panjang menjadi poin-poin utama menggunakan teknologi Large Language Model (LLM) dari OpenAI (GPT-3.5-turbo).

**Dibuat oleh:** Alfredo Michael Alliandaw

## Fitur Utama
* Input teks fleksibel.
* Integrasi API OpenAI yang aman (menggunakan Streamlit Secrets).
* Deployment gratis dan *live* melalui Streamlit Community Cloud.

## Akses Aplikasi (LIVE DEMO)
Anda bisa mencoba aplikasi ini secara langsung di sini:
👉 **[https://ai-summarizer-saya.streamlit.app/](https://ai-summarizer-saya.streamlit.app/)**

## Struktur Teknis
* **Frontend/Hosting:** Streamlit & Streamlit Cloud
* **Backend/Intelligence:** OpenAI API (Python SDK)
* **Security:** Environment Variables (Secrets)
* **Bahasa:** Python 3.11

## Cara Menjalankan Secara Lokal
Untuk menjalankan proyek ini di laptop Anda:
1.  Kloning repository ini.
2.  Install dependencies: `py -3.11 -m pip install -r requirements.txt`
3.  Buat file `.streamlit/secrets.toml` dan masukkan API Key Anda.
4.  Jalankan aplikasi: `py -3.11 -m streamlit run app.py`
