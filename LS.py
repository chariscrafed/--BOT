import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os, random

questions = [
    {"question": "Jika Loid terlalu fokus pada misi tanpa emosi keluarga?",
     "options": ["Misi cepat selesai","Tetap harmonis","Hubungan retak & misi terancam","Tidak berubah"],
     "answer": "C"},
    {"question": "Bagaimana kemampuan Anya bisa jadi kelemahan?",
     "options": ["Lebih pintar","Kewalahan informasi","Tidak perlu belajar","Tidak berpengaruh"],
     "answer": "B"},
    {"question": "Jika identitas Yor terbongkar?",
     "options": ["Tidak ada","Kehilangan kerja","Konflik berbahaya","Terkenal"],
     "answer": "C"},
]
idx, score = 0, 0
BASE = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
root.title("✨ Quiz Spy x Family ✨")
root.geometry("480x720")
root.configure(bg="#0d0d1a")
root.resizable(False, False)

bg = tk.Canvas(root, width=480, height=720, bg="#0d0d1a", highlightthickness=0)
bg.place(x=0, y=0)
random.seed(9)
for _ in range(90):
    x, y = random.randint(0,480), random.randint(0,720)
    c = random.choice(["#ffffff","#ffccee","#ccccff","#aaddff"])
    r = random.choice([1,1,1,2])
    bg.create_oval(x, y, x+r, y+r, fill=c, outline="")
bg.create_oval(-90,-90,190,190, fill="#1e0a3c", outline="")
bg.create_oval(330,560,600,800, fill="#1e0a3c", outline="")

tk.Label(root, text="🌸  SPY x FAMILY QUIZ  🌸",
         font=("Comic Sans MS", 19, "bold"),
         bg="#0d0d1a", fg="#ff79c6").place(x=0, y=22, width=480)
tk.Label(root, text="~ Uji Pengetahuanmu ~",
         font=("Comic Sans MS", 9, "italic"),
         bg="#0d0d1a", fg="#bd93f9").place(x=0, y=58, width=480)

div = tk.Canvas(root, width=480, height=14, bg="#0d0d1a", highlightthickness=0)
div.place(x=0, y=82)
div.create_text(240, 7, text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",
                fill="#ff79c6", font=("Arial", 8))


progress_label = tk.Label(root, text="",
                           font=("Comic Sans MS", 10),
                           bg="#0d0d1a", fg="#8be9fd")
progress_label.place(x=0, y=102, width=480)


qbox = tk.Frame(root, bg="#1a0838", bd=0)
qbox.place(x=28, y=128, width=424)
tk.Canvas(qbox, width=424, height=3, bg="#ff79c6", highlightthickness=0).pack(fill="x")
question_label = tk.Label(qbox, text="", wraplength=380,
                           font=("Comic Sans MS", 12),
                           bg="#1a0838", fg="#f8f8f2",
                           padx=18, pady=16, justify="center")
question_label.pack()
tk.Canvas(qbox, width=424, height=3, bg="#bd93f9", highlightthickness=0).pack(fill="x")


choices    = ["A","B","C","D"]
clr        = ["#ff79c6","#bd93f9","#50fa7b","#ffb86c"]
option_labels = []

ans_frame = tk.Frame(root, bg="#0d0d1a")
ans_frame.place(x=28, y=310, width=424)

for i in range(4):
    row = tk.Frame(ans_frame, bg="#0d0d1a")
    row.pack(fill="x", pady=5)
    tk.Button(row, text=choices[i],
              font=("Arial", 12, "bold"),
              bg=clr[i], fg="#0d0d1a", width=3,
              relief="flat", cursor="hand2",
              activebackground="#ffffff",
              command=lambda c=choices[i]: check_answer(c)).pack(side="left", padx=(0,10))
    lbl = tk.Label(row, text="", font=("Arial", 11),
                   bg="#160630", fg="#f8f8f2",
                   anchor="w", padx=10, pady=5, width=29)
    lbl.pack(side="left")
    option_labels.append(lbl)

tk.Label(root, text="💖  Pilih jawabanmu!  💖",
         font=("Comic Sans MS", 9, "italic"),
         bg="#0d0d1a", fg="#6272a4").place(x=0, y=558, width=480)


frames = []
for i in range(1, 6):
    p = os.path.join(BASE, f"anyaa{i}.png")
    if os.path.exists(p):
        img = Image.open(p).convert("RGBA").resize((72, 72), Image.NEAREST)
        frames.append(ImageTk.PhotoImage(img))

strip = tk.Canvas(root, width=480, height=88, bg="#0d0d1a", highlightthickness=0)
strip.place(x=0, y=628)
strip.create_line(0, 70, 480, 70, fill="#ff79c6", width=1)
strip.create_line(0, 72, 480, 72, fill="#3d1a6e", width=2)
strip.create_text(240, 83, text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",
                  fill="#2a0a4e", font=("Arial", 7))

fi, cx, cd = 0, 0, 1

def animate():
    global fi, cx, cd
    if not frames:
        return
    strip.delete("anya")
    strip.create_image(cx, 34, image=frames[fi],
                       anchor="w" if cd == 1 else "e", tags="anya")
    fi = (fi + 1) % len(frames)
    cx += cd * 3
    if cx >= 480: cd = -1
    elif cx <= 0: cd = 1
    root.after(120, animate)

if frames:
    animate()


def show_question():
    if idx < len(questions):
        q = questions[idx]
        question_label.config(text=q["question"])
        for i in range(4):
            option_labels[i].config(text=q["options"][i])
        progress_label.config(text=f"✦  Soal {idx+1} dari {len(questions)}  ✦")
    else:
        s = "⭐" * score
        messagebox.showinfo("Hasil 🎉",
            f"Skor kamu: {score}/{len(questions)}\n{s}\nGood job~ 💖")
        root.destroy()

def check_answer(choice):
    global idx, score
    if choice == questions[idx]["answer"]:
        score += 1
    idx += 1
    show_question()

show_question()
root.mainloop()
