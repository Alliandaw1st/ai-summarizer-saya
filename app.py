import streamlit as st
from openai import OpenAI # <--- ALAT BARU: Mengambil alat bicara ke AI

# --- 1. Konfigurasi Awal & API Key ---
#] CARA BARU (Mengambil dari secrets.toml)
# Kita ambil kunci yang ada di dalam [openai] -> api_key
try:
    api_key_saya = st.secrets["openai"]["api_key"]
    client = OpenAI(api_key=api_key_saya)
except FileNotFoundError:
    st.error("File .streamlit/secrets.toml tidak ditemukan! Mohon buat dulu.")
    st.stop()
except KeyError:
    st.error("Format di secrets.toml salah. Pastikan ada [openai] dan api_key=...")
    st.stop()

st.set_page_config(page_title="Smart Summarizer", page_icon="💡")
st.title("💡 Asisten Peringkas Dokumen Cerdas")
st.write("Hi, nama saya Alfredo dan ini adalah program pertama saya yang terintegrasi dengan AI.")
st.write("Tempelkan teks atau laporan di bawah ini, dan AI (GPT-3.5) akan meringkasnya untuk Anda.")

# --- 2. Input Teks ---
teks_input = st.text_area("Teks Sumber:", height=300)

# --- 3. Logika AI (Ketika Tombol Ditekan) ---
if st.button("Ringkas Sekarang"):
    if teks_input:
        st.info("Sedang berpikir... Data dikirim ke server OpenAI...")

        try:        
            # Panggil AI: Ini bagian intinya
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", # Model yang dipakai (Stabil dan cepat)
                messages=[
                    # Peran sistem: Kita kasih tahu AI dia harus jadi apa
                    {"role": "system", "content": "Anda adalah asisten yang ahli meringkas teks panjang menjadi 5 poin utama yang jelas dalam Bahasa Indonesia. **Hasil Anda harus selalu dalam format bullet point.**"}, 
                    # Permintaan pengguna
                    {"role": "user", "content": teks_input}
                ]
            )
            )

            # Ambil hasil ringkasan dari jawaban AI
            hasil_ringkasan = response.choices[0].message.content
            
            # Tampilkan Hasil
            st.success("Ringkasan Selesai!")
            st.markdown(f"**Hasil Ringkasan (5 Poin Utama):**\n{hasil_ringkasan}") # Menggunakan markdown agar formatnya bagus

        except Exception as e:
            st.error(f"Terjadi error saat menghubungi AI. Pastikan API Key Anda benar dan saldo akun OpenAI Anda mencukupi. Error: {e}")
    else:

        st.warning("Tolong masukkan teks yang ingin diringkas.")

