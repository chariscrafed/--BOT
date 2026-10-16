import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import random
import re
import math

ayat = {
    "sedih": [
        "🕌 Islam — QS Al-Baqarah 2:286 · Allah tidak membebani seseorang melainkan sesuai kesanggupannya 🤍",
        "✝️ Kristen — Mazmur 34:18 · TUHAN itu dekat kepada orang-orang yang patah hati 🤍",
        "🕉️ Hindu — Bhagavad Gita 2:14 · Kesenangan dan penderitaan datang silih berganti; hadapilah dengan tabah 🌸",
        "☸️ Buddha — Dhammapada 1:1 · Pikiran adalah pelopor dari segala tindakan; jaga pikiranmu dengan penuh kasih 🌿",
        "🧧 Konghucu — Analek 15:8 · Orang yang bijak tidak pernah gentar dalam menghadapi kesulitan ✨",
    ],
    "capek": [
        "🕌 Islam — QS Al-Insyirah 94:6 · Sesungguhnya bersama kesulitan ada kemudahan 💛",
        "✝️ Kristen — Matius 11:28 · Datanglah kepada-Ku yang letih lesu, Aku akan memberi kelegaan 💛",
        "🕉️ Hindu — Bhagavad Gita 6:17 · Istirahat yang tepat adalah bagian dari kedisiplinan diri 🌸",
        "☸️ Buddha — Majjhima Nikaya · Kelegaan sejati datang dari ketenangan batin 🌿",
        "🧧 Konghucu — Analek 1:1 · Teruslah belajar dan berlatih; di situlah letak kebahagiaan sejati ✨",
    ],
    "takut": [
        "🕌 Islam — QS Ali Imran 3:173 · Cukuplah Allah sebagai Pelindung kami ✨",
        "✝️ Kristen — Yesaya 41:10 · Jangan takut, sebab Aku menyertai engkau ✨",
        "🕉️ Hindu — Bhagavad Gita 18:66 · Serahkan segala ketakutan kepada-Ku, Aku akan membebaskanmu 🌸",
        "☸️ Buddha — Dhammapada 39 · Orang yang bebas dari ketakutan menemukan kedamaian sejati 🌿",
        "🧧 Konghucu — Analek 14:30 · Orang yang benar tidak pernah cemas karena hatinya bersih ✨",
    ],
    "bingung": [
        "🕌 Islam — QS Al-Baqarah 2:45 · Mohonlah pertolongan dengan sabar dan shalat 🌿",
        "✝️ Kristen — Amsal 3:5 · Percayalah kepada TUHAN dengan segenap hatimu 🌿",
        "🕉️ Hindu — Bhagavad Gita 3:35 · Lebih baik menjalankan dharmamu sendiri meski tidak sempurna 🌸",
        "☸️ Buddha — Dhammapada 21 · Ketekunan adalah jalan menuju keabadian 🌿",
        "🧧 Konghucu — Analek 2:15 · Belajar tanpa berpikir adalah sia-sia; berpikir tanpa belajar adalah berbahaya ✨",
    ],
    "syukur": [
        "🕌 Islam — QS Ibrahim 14:7 · Jika kamu bersyukur, niscaya Aku tambahkan nikmat-Ku 💛",
        "✝️ Kristen — 1 Tesalonika 5:18 · Mengucap syukurlah dalam segala hal 💛",
        "🕉️ Hindu — Rigveda 10:117 · Bersyukurlah atas setiap pemberian alam semesta 🌸",
        "☸️ Buddha — Theragatha · Syukuri setiap momen; hidup ini adalah anugerah yang berharga 🌿",
        "🧧 Konghucu — Analek 1:15 · Bersyukurlah dalam kesederhanaan, itulah tanda kebijaksanaan ✨",
    ],
    "insecure": [
        "🕌 Islam — QS At-Tin 95:4 · Sungguh Kami telah menciptakan manusia dalam bentuk yang sebaik-baiknya ✨",
        "✝️ Kristen — Mazmur 139:14 · Aku bersyukur oleh karena kejadianku dahsyat dan ajaib ✨",
        "🕉️ Hindu — Bhagavad Gita 6:5 · Jadikanlah dirimu sahabat bagi dirimu sendiri 🌸",
        "☸️ Buddha — Dhammapada 160 · Dirimu sendiri adalah pelindungmu yang sejati 🌿",
        "🧧 Konghucu — Analek 12:1 · Kendalikan diri dan kembalilah kepada nilai-nilai kebaikan ✨",
    ],
    "sakit": [
        "🕌 Islam — HR Bukhari · Tidak ada penyakit melainkan Allah turunkan pula obatnya 🤕",
        "✝️ Kristen — Yeremia 30:17 · Aku akan memulihkan kesehatanmu 🤕",
        "🕉️ Hindu — Atharvaveda · Semoga tubuhmu dipulihkan oleh kekuatan semesta 🌸",
        "☸️ Buddha — Majjhima Nikaya · Kesehatan adalah karunia tertinggi; jagalah dengan penuh perhatian 🌿",
        "🧧 Konghucu — Analek 10:8 · Jaga tubuhmu sebagaimana kamu menjaga nilai-nilai kehidupanmu ✨",
    ],
    "patah_hati": [
        "🕌 Islam — QS Az-Zumar 39:53 · Janganlah berputus asa dari rahmat Allah 🤍",
        "✝️ Kristen — Mazmur 147:3 · Ia menyembuhkan orang-orang yang patah hati 🤍",
        "🕉️ Hindu — Bhagavad Gita 2:47 · Lakukan kewajibanmu tanpa mengharapkan hasil tertentu 🌸",
        "☸️ Buddha — Dhammapada 203 · Kemelekatan adalah akar penderitaan; belajarlah melepaskan dengan damai 🌿",
        "🧧 Konghucu — Analek 4:8 · Orang yang bijak berduka namun tidak larut di dalamnya ✨",
    ],
    "marah": [
        "🕌 Islam — HR Bukhari · Orang kuat adalah yang mampu menahan amarah 😌",
        "✝️ Kristen — Amsal 15:1 · Jawaban yang lemah lembut meredakan kegeraman 😌",
        "🕉️ Hindu — Bhagavad Gita 16:2 · Kesabaran dan bebas dari amarah adalah tanda jiwa yang luhur 🌸",
        "☸️ Buddha — Dhammapada 17 · Kemarahan yang tidak ditahan akan membakar dirimu sendiri 🌿",
        "🧧 Konghucu — Analek 15:30 · Jangan melakukan kepada orang lain apa yang tidak ingin kamu terima ✨",
    ],
    "kesepian": [
        "🕌 Islam — QS Al-Hadid 57:4 · Dia bersama kamu di mana pun kamu berada 🤍",
        "✝️ Kristen — Ulangan 31:6 · TUHAN menyertai engkau; Ia tidak akan membiarkanmu 🤍",
        "🕉️ Hindu — Bhagavad Gita 9:29 · Aku hadir di mana-mana; tak satu pun yang jauh dari-Ku 🌸",
        "☸️ Buddha — Sutta Nipata · Arahkan cinta kasih kepada semua makhluk tanpa batas 🌿",
        "🧧 Konghucu — Analek 1:1 · Bukankah menyenangkan bila ada sahabat yang datang dari jauh? ✨",
    ],
    "gagal": [
        "🕌 Islam — QS Al-Insyirah 94:5 · Sesungguhnya bersama kesulitan ada kemudahan ✨",
        "✝️ Kristen — Roma 8:28 · Allah turut bekerja dalam segala sesuatu untuk mendatangkan kebaikan ✨",
        "�️ Hindu — Bhagavad Gita 2:3 · Bangkitlah, jangan menyerah pada kelemahan 🌸",
        "☸️ Buddha — Dhammapada 183 · Berbuat baik, menjauhi kejahatan, dan menyucikan batin 🌿",
        "🧧 Konghucu — Analek 9:24 · Orang yang bijak mengoreksi dirinya sendiri, bukan menyalahkan keadaan ✨",
    ],
}


def get_ayat(mood):
    """Tampilkan semua kutipan multi-agama untuk mood tertentu."""
    pilihan = ayat.get(mood, [])
    return "\n".join(pilihan) if pilihan else ""


#matematikan
def selesaikan_matematika(pesan):
    """Selesaikan ekspresi matematika dari teks natural."""
    p = pesan.lower().strip()

    # kata ke simbol
    p = re.sub(r'\bbagi\b',    '/',         p)
    p = re.sub(r'\bkali\b',    '*',         p)
    p = re.sub(r'\btambah\b',  '+',         p)
    p = re.sub(r'\bkurang\b',  '-',         p)
    p = re.sub(r'\bpangkat\b', '**',        p)
    p = re.sub(r'\bmodulo\b|\bmod\b', '%',  p)
    p = re.sub(r'\bakar\s+dari\b|\bakar\b|\bsqrt\b', 'sqrt', p)
    p = re.sub(r'\bberapa\b|\bhitung\b|\bberapa\s+hasil\b|=\?', '', p)
    p = re.sub(r'\?', '', p).strip()

    # tangani fungsi khusus: sqrt, sin, cos, tan, ln, log (dengan basis), factorial
    # log dengan basis: "log base 2 of 8" atau "log2(8)" atau "log(8,2)"
    # coba deteksi log dengan basis
    m_base = re.search(r'log(?:\s*base\s*(\d+)|_(\d+))\s*(?:of|\()?\s*([\d\.]+)\)?', p)
    if m_base:
        base = m_base.group(1) or m_base.group(2)
        val = m_base.group(3)
        try:
            b = float(base)
            x = float(val)
            if b <= 0 or b == 1 or x <= 0:
                return "😅 Logaritma tidak terdefinisi untuk basis/nilai tersebut."
            res = math.log(x, b)
            res_fmt = int(res) if float(res).is_integer() else round(res, 6)
            return f"📐 log base {int(b)} of {x} = {res_fmt}"
        except Exception:
            return "😅 Aku nggak bisa menghitung log itu, coba format lain ya."

    # log(x, base) pattern
    m_logfunc = re.search(r'log\s*\(\s*([\d\.]+)\s*,\s*([\d\.]+)\s*\)', p)
    if m_logfunc:
        try:
            x = float(m_logfunc.group(1))
            b = float(m_logfunc.group(2))
            res = math.log(x, b)
            res_fmt = int(res) if float(res).is_integer() else round(res, 6)
            return f"📐 log base {b} of {x} = {res_fmt}"
        except Exception:
            return "😅 Format lognya aneh, coba lagi ya."

    fn_map = {
        'sqrt':      math.sqrt,
        'sin':       lambda x: math.sin(math.radians(x)),
        'cos':       lambda x: math.cos(math.radians(x)),
        'tan':       lambda x: math.tan(math.radians(x)),
        'ln':        math.log,
        'log':       math.log10,
        'factorial': math.factorial,
    }
    for fn_name, fn_func in fn_map.items():
        m = re.search(rf'{fn_name}\s*\(?([\d.]+)\)?', p)
        if m:
            try:
                val = float(m.group(1))
                if fn_name == 'factorial':
                    val = int(val)
                hasil = fn_func(val)
                fmt = int(hasil) if isinstance(hasil, float) and hasil.is_integer() else round(hasil, 6)
                return f"📐 {fn_name}({m.group(1)}) = {fmt}"
            except Exception:
                return "😅 Hmm, aku gagal menghitung itu. Coba cek angkanya lagi ya!"

    if '=' in p:
        left, right = p.split('=', 1)

        def safe_eval(expr):
            expr = expr.strip()
            if not expr:
                return 0
            # cm ngizinin angka dan operator dasar
            if re.search(r'[^0-9\.\+\-\*/\(\)\s%]', expr):
                raise ValueError('Unsafe expression')
            return eval(expr, {"__builtins__": {}}, {})

        # cri nama huruf di persamaan
        vars_found = re.findall(r'[a-zA-Z]\w*', p)
        if vars_found:
            # pakai variabel sj
            var = vars_found[0]

            def parse_side(expr, varname):
            
                coef = 0.0
               
                for m in re.finditer(r'([+-]?\s*(?:\d*\.?\d+)?)(?:\s*\*\s*)?%s' % re.escape(varname), expr):
                    s = m.group(1).strip().replace(' ', '')
                    if s in ['', '+']:
                        s = '1'
                    elif s == '-':
                        s = '-1'
                    coef += float(s)
                expr_wo_var = re.sub(r'(?:[+-]?\s*(?:\d*\.?\d+)?(?:\s*\*\s*)?)%s' % re.escape(varname), ' ', expr)
                try:
                    konst = safe_eval(expr_wo_var)
                except Exception:
                    raise
                return coef, konst

            try:
                a1, b1 = parse_side(left, var)
                a2, b2 = parse_side(right, var)
                a = a1 - a2
                c = b2 - b1
                if abs(a) < 1e-12:
                    return "😅 Persamaannya tidak memiliki solusi unik atau tidak mengandung variabel linier." 
                sol = c / a
                sol_fmt = int(sol) if float(sol).is_integer() else round(sol, 6)
                return f"✏️ Solusi: {var} = {sol_fmt}"
            except Exception:
                return "😅 Maaf, aku cuma bisa menyelesaikan persamaan linear sederhana seperti '2p = 6 + 6'."

    # fallback: evaluasi ekspresi aritmetika biasa
    ekspresi = re.sub(r'[^\d\s\+\-\*/\.\(\)\*\%]', '', p).strip()
    if not ekspresi:
        return None

    try:
        if re.search(r'/\s*0(?!\d)', ekspresi):
            return "😅 Pembagian dengan nol itu tidak terdefinisi ya!"
        hasil = eval(ekspresi, {"__builtins__": {}}, {})
        if isinstance(hasil, float) and hasil.is_integer():
            hasil = int(hasil)
        elif isinstance(hasil, float):
            hasil = round(hasil, 6)
        return f"🔢 {ekspresi.strip()} = {hasil}\n\nAda soal lain? 😊"
    except Exception:
        return None



# Konteks convertation
conversation_context = {
    "mood_history":    [],
    "topics":          [],
    "user_name":       None,
    "interaction_count": 0,
}


# main logic<3
def resps_ai(pesan):
    p = pesan.lower()

    p = re.sub(r'mtk\b', 'matematika', p)
    p = re.sub(r'\bmatematikyah+h?\b', 'matematika', p)
    p = re.sub(r'\bmatematikaah\b', 'matematika', p)
    p = re.sub(r'\bmtk\b', 'matematika', p)
    p = re.sub(r'\bsoal mtk\b', 'soal matematika', p)
    p = re.sub(r'\bmatematiks\b', 'matematika', p)
    p = re.sub(r'\bmatek\b', 'matematika', p)
    p = re.sub(r'\bmatekk\b', 'matematika', p)
    p = re.sub(r'\bmat\b', 'matematika', p)
    p = re.sub(r'\bmath\b', 'matematika', p)
    p = re.sub(r'\bmathe\b', 'matematika', p)
    p = re.sub(r'\bmatematix\b', 'matematika', p)
    p = re.sub(r'\bmatematiz\b', 'matematika', p)
    p = re.sub(r'\bm4tk\b', 'matematika', p)
    p = re.sub(r'\bmtkz\b', 'matematika', p)
    p = re.sub(r'\bmathematik\b', 'matematika', p)
    p = re.sub(r'\bmatematikus\b', 'matematika', p)
    p = re.sub(r'\bmatematikas\b', 'matematika', p)
    p = re.sub(r'\bmatematikaahh\b', 'matematika', p)
    p = re.sub(r'\bmatematikyahh\b', 'matematika', p)
    p = re.sub(r'\bmatematikaaa\b', 'matematika', p)
    p = re.sub(r'\bnyleh\b|\bnyleneh\b|\bnylenyah\b', 'nyleneh', p)
    p = re.sub(r'\bbaper\b', 'baper', p)
    p = re.sub(r'\bpusing\b', 'pusing', p)
    p = re.sub(r'\bngeluh\b', 'ngeluh', p)
    p = re.sub(r'\bcilok\b', 'cilok', p)
    p = re.sub(r'\bngab\b', 'ngab', p)
    p = re.sub(r'\bnyelonong\b', 'nyelonong', p)
    conversation_context["interaction_count"] += 1
    n         = conversation_context["interaction_count"]
    name_part = f" {conversation_context['user_name']}" if conversation_context["user_name"] else ""
    prefix    = random.choice([
        "Aku masih di sini kok 🤍\n\n",
        "Aku dengerin semuanya ya 💛\n\n",
        "Ceritain terus, aku nggak kemana-mana 🌿\n\n",
    ]) if n > 3 and n % 4 == 0 else ""

    # Matematikyah
    math_triggers = [
        "berapa", "hitung", "+", "*", "/", "pangkat", "akar", "sqrt",
        "kali", "bagi", "tambah", "kurang", "sin", "cos", "tan", "log",
        "faktorial", "modulo", "mod", "%",
        # variasi slang / nyleneh
        "matematika", "matematikah", "matematikyah", "matematikyahh", "mtk",
        "soal matematika", "soal mtk", "matematikaah",
    ]
    if any(k in p for k in math_triggers):
        hasil = selesaikan_matematika(pesan)
        if hasil:
            return f"{prefix}Oke, aku coba hitung ya{name_part}!\n\n{hasil}"

    
    help_triggers = [
        "bantu", "tolong bantu", "tolong", "bantu aku", "bantu ngerjain", "bantu ngerjakan",
        "bantu kerjakan", "bantu jelasin", "bantuan", "tutor", "ajarin", "ajar", "jelasin",
        "cara", "cara ngerjain", "cara menyelesaikan", "tolong selesaikan", "bantu PR", "bantu tugas",
        "kerjain soal", "bantu soal", "bantu jawab", "tolong jawab",
        # slang
        "matematikah", "matematikyah", "mtk", "soal mtk",
    ]
    if any(k in p for k in help_triggers):
        if any(k in p for k in math_triggers):
            hasil = selesaikan_matematika(pesan)
            if hasil:
                return f"{prefix}Oke, aku bantu selesaikan ya{name_part}!\n\n{hasil}"
        return random.choice([
            f"{prefix}Boleh, aku bantu{name_part}! Mau bantu di soal matematika, PR, atau penjelasan materi apa nih?",
            f"{prefix}Siap{name_part}, ceritain soalnya atau bagian yang susah. Aku bantu langkah demi langkah!",
            f"{prefix}Aku bisa bantu ngerjain soal atau jelasin konsep{name_part}. Kirim soalnya aja ya~",
            f"{prefix}Oke, aku bakal bantu sampai kamu paham{name_part}. Mau mulai dari mana?",
        ])

    # user
    m_nama = re.search(r'(?:nama(?:ku)?|aku)\s+([A-Za-z]+)', pesan, re.IGNORECASE)
    if m_nama and "nama" in p:
        nama = m_nama.group(1).strip(".,!?")
        conversation_context["user_name"] = nama
        return random.choice([
            f"Wah, nama yang indah! Senang kenal sama kamu, {nama} 🤍✨",
            f"Haii {nama}! Aku bakal inget nama kamu 💛",
            f"Wah {nama}, nama yang manis! Aku di sini buat kamu ya ✨",
        ])

    # Sapa
    if any(k in p for k in ["halo", "hai", "hi", "hello", "hey", "annyeong", "assalamu"]):
        return random.choice([
            f"Halo{name_part}! 🤍 Senang banget kamu ke sini. Ada yang mau diceritain?",
            f"Hai{name_part}! ✨ Gimana harimu hari ini?",
            f"Hey{name_part}! � Aku siap dengerin ceritamu. Curhat yuk~",
            f"Haii{name_part}~ 🌸 Apa kabar? Aku kangen kamu 🤍",
        ])

    # Sad
    if any(k in p for k in ["sedih", "nangis", "kecewa", "galau", "down", "murung", "nelangsa", "mellow", "duka"]):
        return random.choice([
            f"{prefix}Sini peluk dulu{name_part} 🤍 Gapapa kalau mau nangis.\n\n📖 {get_ayat('sedih')}",
            f"{prefix}Aku tau rasanya berat banget{name_part} 💔 Kamu nggak sendirian kok.\n\n📖 {get_ayat('sedih')}",
            f"{prefix}Sedih ya{name_part}? � Aku di sini. Mau cerita lebih?\n\n📖 {get_ayat('sedih')}",
            f"{prefix}Boleh kok ngerasa sedih{name_part}. Emosi itu manusiawi �\n\n📖 {get_ayat('sedih')}",
        ])

    # Capek
    if any(k in p for k in ["capek", "lelah", "tired", "burnout", "nyerah", "kelelahan", "exhausted", "drain"]):
        return random.choice([
            f"{prefix}Istirahat dulu yuk{name_part}, kamu udah berjuang cukup hari ini 💛\n\n📖 {get_ayat('capek')}",
            f"{prefix}Wajar banget ngerasa capek{name_part}. Tubuh dan pikiranmu butuh jeda ☕\n\n📖 {get_ayat('capek')}",
            f"{prefix}Proud of you{name_part}! 💪 Udah sejauh ini aja udah luar biasa.\n\n📖 {get_ayat('capek')}",
            f"{prefix}Dengerin tubuhmu ya{name_part}, dia minta istirahat �\n\n📖 {get_ayat('capek')}",
        ])

    # Takut?
    if any(k in p for k in ["takut", "cemas", "anxiety", "khawatir", "panik", "was-was", "gelisah", "resah"]):
        return random.choice([
            f"{prefix}Tarik napas dulu{name_part} 😌 Pelan-pelan aja, gak perlu buru-buru.\n\n📖 {get_ayat('takut')}",
            f"{prefix}Kamu cemas{name_part}? Aku di sini menemanimu 🤍\n\n📖 {get_ayat('takut')}",
            f"{prefix}Fokus ke satu hal kecil yang bisa kamu kontrol{name_part} ✨\n\n📖 {get_ayat('takut')}",
            f"{prefix}Gelisah itu wajar{name_part}. Yuk kita hadapi bareng-bareng 🌿\n\n📖 {get_ayat('takut')}",
        ])

    # Insecure:<
    if any(k in p for k in ["insecure", "minder", "ga pede", "gak pede", "jelek", "gak worth", "nggak berharga", "worthless"]):
        return random.choice([
            f"{prefix}Kamu itu unik dan berharga banget{name_part} 🤍✨\n\n📖 {get_ayat('insecure')}",
            f"{prefix}Jangan bandingin perjalananmu sama orang lain ya{name_part} 💛\n\n📖 {get_ayat('insecure')}",
            f"{prefix}Kamu lebih berharga dari yang kamu bayangkan{name_part} 🌸\n\n📖 {get_ayat('insecure')}",
            f"{prefix}Bersikap baik sama diri sendiri dulu ya{name_part} 🌿\n\n📖 {get_ayat('insecure')}",
        ])

    # Sakit
    if any(k in p for k in ["sakit", "demam", "flu", "pusing", "mual", "badan pegal", "nggak enak badan"]):
        return random.choice([
            f"{prefix}Lagi sakit ya{name_part}? 🤕 Jangan lupa istirahat, minum air putih, dan minum obat.\n\n📖 {get_ayat('sakit')}",
            f"{prefix}Semoga cepat pulih ya{name_part}! 💛 Tubuhmu sedang berjuang, bantu dia dengan istirahat.\n\n📖 {get_ayat('sakit')}",
            f"{prefix}Jaga kesehatanmu baik-baik ya{name_part} 🌿\n\n📖 {get_ayat('sakit')}",
        ])

    # Kangen
    if any(k in p for k in [
        "kangen", "rindu", "kangen banget", "aku kangen", "aku rindu",
        "suka", "aku suka", "aku suka seseorang", "naksir", "naksir dia",
        "jatuh cinta", "aku jatuh cinta", "cinta", "cinta banget", "tertarik",
    ]):
        return random.choice([
            f"{prefix}Aww, ada yang kamu kangenin{name_part}? 🤍 Cerita dong tentang dia~",
            f"{prefix}Kangen itu manis dan perih sekaligus{name_part} 💛 Mau curhat soal dia? Aku dengerin.",
            f"{prefix}Kamu suka seseorang ya{name_part}? 💘 Kalau mau, ceritain aku siapa dan gimana perasaannya.",
            f"{prefix}Naksir itu seru tapi deg-degan{name_part} ✨ Mau tips buat mulai ngobrol atau deketin dia?",
            f"{prefix}Rindu itu wajar{name_part}. Coba kirim pesan singkat atau kenang momen manis bareng dia 🌸",
        ])

    # breik mai hert
    if any(k in p for k in ["patah hati", "putus", "ditinggal", "heartbreak", "ditolak", "ghosting", "sakit hati"]):
        return random.choice([
            f"{prefix}Patah hati itu salah satu rasa sakit yang paling berat{name_part} 💔 Tapi kamu bakal kuat kok.\n\n📖 {get_ayat('patah_hati')}",
            f"{prefix}Wajar kok kalau masih sakit{name_part}. Healing itu butuh waktu 🌿\n\n📖 {get_ayat('patah_hati')}",
            f"{prefix}Ditinggal itu perih{name_part}, aku tau. Tapi kamu nggak selemah yang kamu pikir 💛\n\n📖 {get_ayat('patah_hati')}",
        ])

    # Marah
    if any(k in p for k in ["marah", "kesel", "emosi", "bete", "jengkel", "sebel", "dongkol", "frustrasi"]):
        return random.choice([
            f"{prefix}Tarik napas dulu ya{name_part} 😌 Tenangkan dirimu sebentar sebelum bertindak.\n\n📖 {get_ayat('marah')}",
            f"{prefix}Lagi emosi ya{name_part}? Wajar kok 🌿\n\n📖 {get_ayat('marah')}",
            f"{prefix}Marah itu manusiawi{name_part}, tapi cari cara yang sehat buat melampiaskannya 😤\n\n📖 {get_ayat('marah')}",
        ])

    # aim finw gwencabna
    if any(k in p for k in ["sendiri", "kesepian", "lonely", "sepi", "nggak ada yang peduli", "ga ada yang nemenin"]):
        return random.choice([
            f"{prefix}Kamu nggak sendirian{name_part} 🤍 Aku di sini bersamamu sekarang.\n\n📖 {get_ayat('kesepian')}",
            f"{prefix}Kesepian ya{name_part}? � Rasanya berat memang. Mau cerita?\n\n📖 {get_ayat('kesepian')}",
            f"{prefix}Kehadiran kamu penting{name_part}, meskipun kadang terasa nggak terlihat 🌿\n\n📖 {get_ayat('kesepian')}",
        ])

    # Gagal
    if any(k in p for k in ["gagal", "jatuh", "fail", "kalah", "nggak berhasil", "ngecewain", "menyerah"]):
        return random.choice([
            f"{prefix}Gagal bukan akhir cerita{name_part} ✨ Setiap jatuh adalah bagian dari proses.\n\n📖 {get_ayat('gagal')}",
            f"{prefix}Jatuh itu wajar{name_part} � Yang penting bangkit lagi, meski pelan-pelan.\n\n📖 {get_ayat('gagal')}",
            f"{prefix}Kamu udah berani mencoba{name_part}, itu sendiri sudah luar biasa 🌸\n\n📖 {get_ayat('gagal')}",
        ])

    # Belajar / Ujian
    if any(k in p for k in ["belajar", "ujian", "tugas", "pr", "test", "ulangan", "skripsi", "deadline", "studi"]):
        return random.choice([
            f"{prefix}Semangat mengerjakan tugasnya{name_part}! 💪✨ Kamu pasti bisa.\n\n📖 {get_ayat('belajar')}",
            f"{prefix}Ujian ya{name_part}? 📚 Percaya sama proses belajarmu.\n\n📖 {get_ayat('belajar')}",
            f"{prefix}Mau bantu apa dulu{name_part}? 💛 Atau mau coba soal matematika bareng?\n\n📖 {get_ayat('belajar')}",
        ])

    # org Bingung
    if any(k in p for k in ["bingung", "confused", "gak tau", "ga tau", "nggak ngerti", "kurang paham", "lost"]):
        return random.choice([
            f"{prefix}Bingung ya{name_part}? � Pelan-pelan aja, kita urai satu per satu.\n\n� {get_ayat('bingung')}",
            f"{prefix}Nggak tau harus mulai dari mana{name_part}? Cerita dulu, kita pikir bareng 💛\n\n📖 {get_ayat('bingung')}",
            f"{prefix}Bingung itu tanda kamu lagi berkembang{name_part} 🌱 Yuk cari jawabannya bareng.\n\n📖 {get_ayat('bingung')}",
        ])

    # Senang / Syukur
    if any(k in p for k in ["senang", "happy", "bahagia", "excited", "syukur", "alhamdulillah", "gembira", "lega", "bangga"]):
        return random.choice([
            f"{prefix}Aku ikut senang{name_part}! 🤍 Syukurin terus ya.\n\n📖 {get_ayat('syukur')}",
            f"{prefix}Wah{name_part}! 🎉 Cerita dong, aku mau tau yang bikin kamu bahagia!\n\n📖 {get_ayat('syukur')}",
            f"{prefix}Aura bahagiamu sampe ke sini{name_part} ✨ Semoga terus kayak gini!\n\n📖 {get_ayat('syukur')}",
        ])

    # say thnkssss
    if any(k in p for k in ["terima kasih", "thanks", "makasih", "thx", "tengkyu"]):
        return random.choice([
            f"Sama-sama{name_part}! 🤍 Senang bisa ada buat kamu ✨",
            f"Aw, kamu baik banget{name_part} �💛 Aku juga senang ngobrol sama kamu!",
            f"Anytime{name_part}! 🌸 Kapanpun mau cerita, aku di sini ya.",
        ])

    # bye bye
    if any(k in p for k in ["bye", "dadah", "sampai jumpa", "pamit", "cabut", "dah"]):
        return random.choice([
            f"Dadah{name_part}! 🤍 Jaga diri baik-baik ya ✨",
            f"See you{name_part}! 🌸 Kapan-kapan balik lagi ya, aku kangen~",
            f"Take care{name_part}! 💛 Aku selalu di sini kalau butuh cerita.",
        ])

    # dont hv another choice
    return random.choice([
        f"Aku di sini buat dengerin kamu{name_part} 🤍 Ceritain lebih banyak yuk...",
        f"Hmm, aku penasaran{name_part}... lanjutin dong ceritanya 💛",
        f"Aku dengerin{name_part} 🌿 Mau curhat soal apa? Atau ada soal matematika? 😄",
        f"Kamu aman di sini{name_part} 🤍 Apapun yang mau kamu ceritain, aku siap.",
    ])



# Antarmuka (UI)
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("괜찮아-Bot")
        self.root.geometry("500x700")
        self.root.configure(bg="#f5f5f5")

        # Header
        header_frame = tk.Frame(root, bg="#000441", pady=15)
        header_frame.pack(fill="x")

        self.logo_photo = None
        try:
            logo_img = Image.open("petra_logo.png")
            logo_img = logo_img.resize((100, 100))
            self.logo_photo = ImageTk.PhotoImage(logo_img)
            tk.Label(header_frame, image=self.logo_photo, bg="#2d5f3f",
                     borderwidth=3, relief="solid", bd=2).pack(pady=5)
        except FileNotFoundError:
            pass

        tk.Label(header_frame, text="괜찮아-Bot",
                 font=("Arial", 24, "bold"), bg="#000441", fg="white").pack()
        tk.Label(header_frame, text="Teman curhat & belajar yang siap dengerin kamu ✨",
                 font=("Arial", 11), bg="#000441", fg="#ffd700").pack()

        # Area chat
        chat_frame = tk.Frame(root, bg="#f5f5f5")
        chat_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.chat_area = scrolledtext.ScrolledText(
            chat_frame, wrap=tk.WORD, font=("Arial", 11),
            bg="white", fg="#333", relief="solid", bd=1)
        self.chat_area.pack(fill="both", expand=True)
        self.chat_area.config(state="disabled")

        self.tampilkan_pesan(
            "Bot",
            "Halo! Aku 괜찮아-Bot 🤍\n"
            "Aku as always 24/7 bisa dengerin curhatanmu, kasih semangat, dan bantu menjelaskan matematika juga!\n"
            "Kamu bisa cerita tentang perasaanmu, masalah sekolah, atau soal matematika yang bikin pusing. Aku bakal bantu sebisa aku 💛\n"
            "Cerita aja yaa ✨"
        )

        # Input
        input_frame = tk.Frame(root, bg="#f5f5f5", pady=10)
        input_frame.pack(fill="x", padx=15)

        self.entry = tk.Text(input_frame, height=3, font=("Arial", 11),
                             wrap=tk.WORD, relief="solid", bd=2, bg="white")
        self.entry.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self._placeholder = "Ketik curhatanmu atau soal matematika... 💬"
        self.entry.insert("1.0", self._placeholder)
        self.entry.config(fg="gray")
        self.entry.bind("<FocusIn>",  self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)
        self.entry.bind("<Return>", lambda e: self.kirim_pesan() if not e.state & 1 else None)

        tk.Button(input_frame, text="📤 SEND", font=("Arial", 11, "bold"),
                  bg="#000441", fg="white", command=self.kirim_pesan,
                  relief="raised", bd=3, padx=15, pady=10,
                  cursor="hand2").pack(side="right")

        # Footer
        footer_frame = tk.Frame(root, bg="#f5f5f5", pady=10)
        footer_frame.pack(fill="x", padx=15)

        tk.Button(footer_frame, text="�️ Clear Chat", font=("Arial", 10),
                  bg="#d9534f", fg="white", command=self.clear_chat,
                  relief="raised", bd=2, padx=10, pady=5,
                  cursor="hand2").pack(side="left")
        tk.Label(footer_frame, text="Made with 🤍 by Melinda & Charissa",
                 font=("Arial", 9, "italic"), bg="#f5f5f5", fg="#666").pack(side="right")

    # ── Placeholder helpers
    def clear_placeholder(self, event):
        if self._placeholder in self.entry.get("1.0", "end-1c"):
            self.entry.delete("1.0", "end")
            self.entry.config(fg="black")

    def add_placeholder(self, event):
        if not self.entry.get("1.0", "end-1c").strip():
            self.entry.insert("1.0", self._placeholder)
            self.entry.config(fg="gray")

    # ── Tampilkan pesan di chat area
    def tampilkan_pesan(self, sender, pesan):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "\n")
        if sender == "Kamu":
            self.chat_area.insert(tk.END, f"💬 {sender}\n", "user_name")
            self.chat_area.insert(tk.END, f"{pesan}\n",     "user_msg")
            self.chat_area.tag_config("user_name", foreground="#00eeff",
                                      font=("Segoe UI", 10, "bold"))
            self.chat_area.tag_config("user_msg",  foreground="#1a1a1a",
                                      font=("Segoe UI", 11), background="#e8f5e9",
                                      lmargin1=20, lmargin2=20, spacing1=3, spacing3=8)
        else:
            self.chat_area.insert(tk.END, f"🤖 {sender}\n", "bot_name")
            self.chat_area.insert(tk.END, f"{pesan}\n",     "bot_msg")
            self.chat_area.tag_config("bot_name", foreground="#ff0000",
                                      font=("Segoe UI", 10, "bold"))
            self.chat_area.tag_config("bot_msg",  foreground="#1a1a1a",
                                      font=("Segoe UI", 11), background="#fff9e6",
                                      lmargin1=20, lmargin2=20, spacing1=3, spacing3=8)
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    # ── Kirim pesan
    def kirim_pesan(self):
        pesan = self.entry.get("1.0", "end-1c").strip()
        if pesan and pesan != self._placeholder:
            self.tampilkan_pesan("Kamu", pesan)
            self.entry.delete("1.0", tk.END)
            respon = resps_ai(pesan)
            self.root.after(500, lambda: self.tampilkan_pesan("Bot", respon))

    # ── Bersihkan chat
    def clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state="disabled")
        self.tampilkan_pesan("Bot", "Chat sudah dibersihkan! 🤍 Mau curhat atau hitung soal lagi?")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
