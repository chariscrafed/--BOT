import tkinter as tk
import subprocess
import sys
import os
from PIL import Image, ImageTk

BASE = os.path.dirname(os.path.abspath(__file__))

BG = "#111827"
HEADER_BG = "#1F2937"
ACCENT = "#8BAFC4"
ACCENT_HOVER = "#7298AF"
CARD_BG = "#FFFFFF"
CONTENT_BG = "#F1F5F9"
TEXT_DARK = "#243447"
TEXT_MUTED = "#64748B"
TEXT_LIGHT = "#F8FAFC"
DIVIDER = "#DCE5EC"

root = tk.Tk()
root.title("CHARRRRRRRRRRRRRRRRRRRRR")
root.geometry("500x660")
root.configure(bg=BG)
root.resizable(False, False)

header = tk.Frame(root, bg=HEADER_BG, pady=0)
header.pack(fill="x")

logo_photo = None
logo_path = os.path.join(BASE, "")
try:
    img = Image.open(logo_path).convert("RGBA")
    w, h = img.size
    pixels = img.load()

    from collections import deque
    visited = [[False] * h for _ in range(w)]

    def is_white(x, y):
        r, g, b, a = pixels[x, y]
        return r > 200 and g > 200 and b > 200

    queue = deque()
    for x in range(w):
        for y in [0, h - 1]:
            if not visited[x][y] and is_white(x, y):
                queue.append((x, y))
                visited[x][y] = True
    for y in range(h):
        for x in [0, w - 1]:
            if not visited[x][y] and is_white(x, y):
                queue.append((x, y))
                visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for nx, ny in [(cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)]:
            if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny] and is_white(nx, ny):
                visited[nx][ny] = True
                queue.append((nx, ny))

    img = img.resize((80, 80), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(img)
    tk.Label(header, image=logo_photo, bg=HEADER_BG).pack(pady=(18, 6))
except Exception:
    tk.Label(header, text="🏫", font=("Arial", 36),
             bg=HEADER_BG, fg=ACCENT).pack(pady=(18, 6))

tk.Label(header, text="",
         font=("Arial", 11, "italic"),
         bg=HEADER_BG, fg=ACCENT).pack()

tk.Label(header, text="Welcome Home",
         font=("Arial", 20, "bold"),
         bg=HEADER_BG, fg=TEXT_LIGHT).pack(pady=(4, 2))

tk.Label(header, text="Pilih aplikasi yang mau kamu buka ✨",
         font=("Arial", 10),
         bg=HEADER_BG, fg="#FFFB00").pack(pady=(0, 16))

tk.Canvas(root, height=4, bg=ACCENT,
          highlightthickness=0).pack(fill="x")


def make_card(parent, number, emoji, title, desc, btn_text, accent, cmd):
    outer = tk.Frame(parent, bg=accent, bd=0)
    outer.pack(fill="x", padx=30, pady=(20, 0))

    bar = tk.Frame(outer, bg=accent, width=6)
    bar.pack(side="left", fill="y")

    card = tk.Frame(outer, bg=CARD_BG, pady=16, padx=20)
    card.pack(side="left", fill="both", expand=True)

    top = tk.Frame(card, bg=CARD_BG)
    top.pack(fill="x")

    badge = tk.Label(
        top, text=f" {number} ",
        font=("Arial", 11, "bold"),
        bg=accent, fg=TEXT_DARK,
        padx=6, pady=2
    )
    badge.pack(side="left", padx=(0, 10))

    tk.Label(
        top, text=f"{emoji}  {title}",
        font=("Arial", 14, "bold"),
        bg=CARD_BG, fg=TEXT_DARK
    ).pack(side="left")

    tk.Canvas(
        card, height=1, bg=DIVIDER,
        highlightthickness=0
    ).pack(fill="x", pady=(10, 8))

    tk.Label(
        card, text=desc,
        font=("Arial", 10),
        bg=CARD_BG, fg=TEXT_MUTED,
        wraplength=360, justify="left"
    ).pack(anchor="w")

    tk.Button(
        card, text=btn_text,
        font=("Arial", 10, "bold"),
        bg=accent, fg=TEXT_DARK,
        relief="flat", cursor="hand2",
        activebackground=ACCENT_HOVER,
        activeforeground=TEXT_LIGHT,
        padx=16, pady=7,
        command=cmd
    ).pack(anchor="w", pady=(12, 0))


def launch(filename):
    subprocess.Popen([sys.executable, os.path.join(BASE, filename)])


content = tk.Frame(root, bg=CONTENT_BG)
content.pack(fill="both", expand=True)

make_card(
    content,
    number="01",
    emoji="🎮",
    title="Spy x Family Quiz",
    desc="Uji pengetahuanmu tentang Spy x Family!\nJawab 3 soal seru bareng Anya dan lihat skor akhirmu. 🌸",
    btn_text="▶   Buka Quiz Game",
    accent=ACCENT,
    cmd=lambda: launch("LS.py"),
)

make_card(
    content,
    number="02",
    emoji="🤍",
    title="괜찮아-Bot",
    desc="Curhat sama bot yang siap dengerin kamu kapan aja.\nDilengkapi ayat-ayat penguatan. ✨",
    btn_text="▶   Buka Chatbot",
    accent=ACCENT,
    cmd=lambda: launch("chr.py"),
)

tk.Canvas(
    root, height=1, bg=DIVIDER,
    highlightthickness=0
).pack(fill="x", pady=(24, 0))

tk.Label(
    root,
    text="Made with 🤍 by Charissa  •  SMA Pembangunan Jaya 2",
    font=("Arial", 9, "italic"),
    bg=BG, fg="#A8B6C7"
).pack(pady=10)

root.mainloop()