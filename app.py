import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("planer.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS zavdannya(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
)
""")
conn.commit()

def zavantazhiti():
    spysok.delete(0, tk.END)
    cursor.execute("SELECT id, text FROM zavdannya")
    for row in cursor.fetchall():
        spysok.insert(tk.END, f"{row[0]}. {row[1]}")

def dodaty():
    text = pole.get()
    if text.strip() == "":
        messagebox.showwarning("Помилка", "Введіть завдання")
        return
    cursor.execute("INSERT INTO zavdannya(text) VALUES(?)", (text,))
    conn.commit()
    pole.delete(0, tk.END)
    zavantazhiti()

def vydalyty():
    try:
        vib = spysok.get(spysok.curselection())
        id_zavd = vib.split(".")[0]
        cursor.execute("DELETE FROM zavdannya WHERE id=?", (id_zavd,))
        conn.commit()
        zavantazhiti()
    except:
        messagebox.showwarning("Помилка", "Оберіть завдання")

root = tk.Tk()
root.title("Планувальник")
root.geometry("400x500")
root.config(bg="#2b2b2b")

zag = tk.Label(root, text="Мій планувальник", font=("Arial", 18, "bold"), bg="#2b2b2b", fg="white")
zag.pack(pady=10)

pole = tk.Entry(root, font=("Arial", 14))
pole.pack(pady=10, padx=20, fill="x")

btn1 = tk.Button(root, text="Додати завдання", font=("Arial", 12), bg="#4CAF50", fg="white", command=dodaty)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Видалити завдання", font=("Arial", 12), bg="#f44336", fg="white", command=vydalyty)
btn2.pack(pady=5)

spysok = tk.Listbox(root, font=("Arial", 12), bg="#1e1e1e", fg="white")
spysok.pack(pady=20, padx=20, fill="both", expand=True)

zavantazhiti()

root.mainloop()