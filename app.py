import streamlit as st
import random
import urllib.parse

st.set_page_config(page_title="404.fm", page_icon="🟢", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #121212; color: white; }
    .card { background-color: #181818; padding: 20px; border-radius: 12px; border: 2px solid #1DB954; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

data_vibe = {
    "1. OMG DIKEJAR DEADLINE": {
        "lagu": ["Hindia - Evaluasi", "Tulus - Manusia Kuat", "Nadin Amizah - Bertaut", "Sal Priadi - Gala Bunga Matahari", "Feby Putri - Runtuh", "Hindia - Secukupnya", "Tulus - Diri", "Idgitaf - Takut", "Coldplay - Fix You", "Kunto Aji - Rehat"],
        "julukan": ["pejuang tugas", "kurang tidur", "butuh kopi", "lembur terus"],
        "saran": "kerjain pelan-pelan aja, yang penting selesai tepat waktu."
    },
    "2. Falling in love": {
        "lagu": ["Hivi! - Remaja", "Rizky Febian - Bermuara", "Taylor Swift - Lover", "Yovie & Nuno - Janji Suci", "Nadhif Basalamah - Penjaga Hati", "Sal Priadi - Dari Planet Lain", "Maliq & D'Essentials - Adu Rayu", "Tiara Andini - Kupu-Kupu", "Bruno Major - Easily", "Maliq & D'Essentials - Kita Bikin Romantis"],
        "julukan": ["lagi senyum-senyum sendiri", "mood bagus", "full senyum"],
        "saran": "semoga harimu lancar terus ya, jangan lupa sapa dia."
    },
    "3. Mode lock in boss": {
        "lagu": ["Imagine Dragons - Believer", "OneRepublic - Counting Stars", "Eminem - Lose Yourself", "Feast - Peradaban", "The Script - Hall of Fame", "Alan Walker - Faded", "Queen - Don't Stop Me Now", "Kanye West - Stronger", "Blackpink - How You Like That", "NewJeans - Super Shy"],
        "julukan": ["lagi fokus banget", "mode serius", "anti ganggu", "produktif"],
        "saran": "fokusmu lagi bagus banget, lanjutin sampai target hari ini beres."
    },
    "4. Chill": {
        "lagu": ["Juicy Luicy - Sialan", "Bernadya - Untungnya, Bumi Masih Berputar", "Reality Club - Anything You Want", "Hindia - Rumah Ke Rumah", "Sheila On 7 - Hari Bersamanya", "RAN - Dekat di Hati", "Lomba Sihir - Hati dan Paru-Paru", "Bruno Mars - Leave The Door Open", "NIKI - Every Summertime", "Payung Teduh - Angin Pujaan Hujan"],
        "julukan": ["mode santai", "bebas tugas", "waktunya istirahat", "jam kosong"],
        "saran": "nikmatin waktu santaimu, sekali-sekali istirahat itu wajib."
    },
    "5. GAMOOONNNN": {
        "lagu": ["Bernadya - Satu Bulan", "Bernadya - Kata Mereka Ini Berlebihan", "Bernadya - Lama-Lama", "Bernadya - Kini Mereka Tahu", "Juicy Luicy - Lantas", "Juicy Luicy - Tampar", "Juicy Luicy - Tanpa Tergesa", "Juicy Luicy - Mawar Jingga", "Mahalini - Sial", "Mahalini - Melawan Restu"],
        "julukan": ["lagi kepikiran masa lalu", "susah move on", "galau tengah malam"],
        "saran": "dengerin lagunya sampai puas, habis itu pelan-pelan lupain ya."
    }
}

st.markdown("<h1 style='text-align: center; color: #1DB954;'>🟢 404.fm</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #B3B3B3; font-style: italic;'>curated for your current state.</p>", unsafe_allow_html=True)
st.write("---")

nama = st.text_input("nama kamu:")
mood = st.selectbox("mood hari ini:", list(data_vibe.keys()))
energi = st.slider("sisa energi:", 0, 100, 75)

if st.button("cek hasil", type="primary"):
    if nama.strip() == "":
        st.warning("isi dulu nama kamu ya!")
    else:
        info = data_vibe[mood]
        lagu_pilihan = random.choice(info["lagu"])
        status_terpilih = random.choice(info["julukan"])
        
        bonus_hoki = [random.randint(10, 30) for _ in range(2)]
        skor_hoki = min(100, (energi // 2) + sum(bonus_hoki))
        
        if energi >= 80:
            teks_energi = f"energi: {energi}% (masih seger banget)"
        elif energi >= 40:
            teks_energi = f"energi: {energi}% (mulai capek dikit)"
        else:
            teks_energi = f"energi: {energi}% (butuh kasur sekarang juga)"
            
        st.markdown(f"""
            <div class="card">
                <h3 style="color: #FFFFFF; text-align: center;">playlist buat {nama}</h3>
                <p style="color: #FACC15; text-align: center; font-weight: bold;">status: {status_terpilih}</p>
                <div style="background-color: #282828; padding: 12px; border-radius: 8px; text-align: center; margin: 10px 0;">
                    <b>lagu buat kamu:</b><br>{lagu_pilihan}
                </div>
                <p style="color: #B3B3B3;">⚡ {teks_energi}</p>
                <p style="color: #38BDF8;">🍀 hoki hari ini: {skor_hoki}%</p>
                <p style="color: #B3B3B3; font-style: italic; text-align: center;">catatan: "{info['saran']}"</p>
            </div>
        """, unsafe_allow_html=True)
        
        query = urllib.parse.quote(lagu_pilihan)
        url_spotify = f"https://open.spotify.com/search/{query}"
        st.markdown(f"<a href='{url_spotify}' target='_blank'><button style='width: 100%; background-color: #1DB954; color: #121212; padding: 10px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; margin-top: 10px;'>putar di Spotify ↗</button></a>", unsafe_allow_html=True)