import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

class GestionCalendario:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendario Mario")
        self.master.geometry("420x470")
        self.master.configure(bg="#2d2d4f")

        tk.Label(master, text="Selecciona una fecha", font=("Arial Black", 18, "bold"),
                 bg="#2d2d4f", fg="#ffd700").pack(pady=18)

        self.calendario = Calendar(master, selectmode='day',
                                  year=datetime.now().year,
                                  month=datetime.now().month,
                                  day=datetime.now().day,
                                  font=("Arial", 12),
                                  background="#a0e7e5", foreground="#222",
                                  bordercolor="#3a00ce", headersbackground="#3a00ce",
                                  headersforeground="#fff", selectbackground="#ffd700",
                                  selectforeground="#222", weekendbackground="#e3f3e9",
                                  weekendforeground="#3a00ce")
        self.calendario.pack(pady=10)

        self.btn_seleccionar = tk.Button(master, text="Seleccionar Fecha",
                                         command=self.mostrar_fecha,
                                         font=("Arial", 13, "bold"),
                                         bg="#3a00ce", fg="#fff",
                                         relief=tk.RAISED, bd=3,
                                         activebackground="#5e3cff",
                                         width=20, height=2)
        self.btn_seleccionar.pack(pady=18)

        self.lbl_fecha = tk.Label(master, text="", font=("Arial Black", 14),
                                 bg="#2d2d4f", fg="#a0e7e5")
        self.lbl_fecha.pack(pady=10)

    def mostrar_fecha(self):
        fecha_seleccionada = self.calendario.get_date()
        self.lbl_fecha.config(text=f"Fecha seleccionada: {fecha_seleccionada}")
        messagebox.showinfo("Fecha seleccionada", f"Has seleccionado: {fecha_seleccionada}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionCalendario(root)
    root.mainloop()