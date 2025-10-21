import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from collections import deque
from datetime import datetime

# Clase para almacenar la información del usuario
class EstructuraDatosUsuario:
    def __init__(self, id_type, id_number, name, age, estrato, atencion, valor_copago, fecha_registro):
        self.id_type = id_type
        self.id_number = id_number
        self.name = name
        self.age = age
        self.estrato = estrato
        self.atencion = atencion
        self.valor_copago = valor_copago
        self.fecha_registro = fecha_registro

# Funciones para calcular el copago
def calcular_copago(estrato, tipo_atencion):
    if tipo_atencion == 'Medicina General':
        tabla = {1:0, 2:0, 3:10000, 4:15000, 5:20000, 6:30000}
    elif tipo_atencion == 'Examen Laboratorio':
        tabla = {1:0, 2:0, 3:0, 4:5000, 5:10000, 6:20000}
    else:
        tabla = {}
    return tabla.get(estrato, 0)

# Ventana principal
class App:
    def __init__(self, root):
        self.root = root
        # Ajustes para ventana más compacta y no redimensionable
        self.root.title("Login - Salvando Vidas")
        self.root.geometry("1920x1080")   # tamaño más pequeño y controlado
        self.root.resizable(False, False)

        self.pila = []
        self.cola = deque()
        self.lista = []

        # Login Frame
        self.login_frame  = tk.Frame(root, padx=8, pady=8)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Contraseña:", font=("Arial", 10)).grid(row=0, column=0, sticky='e', padx=4, pady=4)
        self.password_entry = tk.Entry(self.login_frame, show='*', width=20)
        self.password_entry.grid(row=0, column=1, padx=4, pady=4)

        self.btn_ingresar = tk.Button(self.login_frame, text="Ingresar", command=self.validar_contraseña, width=12)
        self.btn_ingresar.grid(row=1, column=0, pady=6, padx=4)
        self.btn_salir = tk.Button(self.login_frame, text="Salir", command=root.quit, width=12)
        self.btn_salir.grid(row=1, column=1, pady=6, padx=4)

        # Botón Acerca de en la esquina superior derecha sin bordes
        self.btn_acerca = tk.Button(self.root, text="Acerca de", command=self.mostrar_acerca,
                                    borderwidth=0, relief="flat", bg=self.root.cget("bg"))
        self.btn_acerca.place(relx=1.0, rely=0, anchor="ne", x=-1500, y=10)

        # Ventana de ingreso de datos (después del login)
        self.frm_control = None

    def validar_contraseña(self):
        clave = self.password_entry.get()
        if clave == 'unad':
            self.login_frame.destroy()
            self.mostrar_formulario()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")

    def mostrar_acerca(self):
        info = ("App salvando vidas Eps - en Python\n"
                "Universidad Nacional Abierta y a Distancia - UNAD\n"
                "librerias usadas: Tkinter\n"
                "Estudiante: Mario andres Garavito\n"
                "Grupo: 301305_155\n")
        messagebox.showinfo("Acerca de", info)

    def mostrar_formulario(self):
        # Contenedor principal reducido para que la ventana no sea tan grande
        self.frm_control = tk.Frame(self.root, padx=6, pady=6)
        self.frm_control.pack(padx=8, pady=8, fill='both', expand=True)

        # Sección de ingreso de datos (lado izquierdo)
        frame_datos = ttk.LabelFrame(self.frm_control, text="Registro de Usuario", width=360)
        frame_datos.grid(row=0, column=0, padx=6, pady=6, sticky='n')

        # Campos (tamaño compacto)
        ttk.Label(frame_datos, text="Tipo ID:").grid(row=0, column=0, sticky='e', padx=4, pady=2)
        self.tipo_id = ttk.Combobox(frame_datos, values=["CC", "CE", "NUIP", "PAS"], state='readonly', width=18)
        self.tipo_id.grid(row=0, column=1, padx=4, pady=2)

        ttk.Label(frame_datos, text="Número ID:").grid(row=1, column=0, sticky='e', padx=4, pady=2)
        self.num_id = ttk.Entry(frame_datos, width=20)
        self.num_id.grid(row=1, column=1, padx=4, pady=2)

        ttk.Label(frame_datos, text="Nombre:").grid(row=2, column=0, sticky='e', padx=4, pady=2)
        self.nombre = ttk.Entry(frame_datos, width=20)
        self.nombre.grid(row=2, column=1, padx=4, pady=2)

        ttk.Label(frame_datos, text="Edad:").grid(row=3, column=0, sticky='e', padx=4, pady=2)
        self.edad = ttk.Entry(frame_datos, width=6)
        self.edad.grid(row=3, column=1, sticky='w', padx=4, pady=2)

        ttk.Label(frame_datos, text="Estrato:").grid(row=4, column=0, sticky='e', padx=4, pady=2)
        self.estrato = ttk.Combobox(frame_datos, values=["1","2","3","4","5","6"], state='readonly', width=6)
        self.estrato.grid(row=4, column=1, sticky='w', padx=4, pady=2)

        ttk.Label(frame_datos, text="Atención:").grid(row=5, column=0, sticky='e', padx=4, pady=2)
        self.tipo_atencion = tk.StringVar()
        ttk.Radiobutton(frame_datos, text="Medicina General", variable=self.tipo_atencion, value='Medicina General').grid(row=5, column=1, sticky='w')
        ttk.Radiobutton(frame_datos, text="Examen Lab.", variable=self.tipo_atencion, value='Examen Laboratorio').grid(row=6, column=1, sticky='w')

        ttk.Label(frame_datos, text="Fecha:").grid(row=7, column=0, sticky='e', padx=4, pady=2)
        self.fecha_registro = ttk.Entry(frame_datos, width=12)
        self.fecha_registro.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.fecha_registro.grid(row=7, column=1, sticky='w', padx=4, pady=2)

        ttk.Label(frame_datos, text="Valor Copago:").grid(row=8, column=0, sticky='e', padx=4, pady=2)
        self.valor_copago_var = tk.StringVar()
        self.valor_copago = ttk.Entry(frame_datos, textvariable=self.valor_copago_var, state='readonly', width=12)
        self.valor_copago.grid(row=8, column=1, sticky='w', padx=4, pady=2)

        # Botones compactos
        self.btn_calcular = ttk.Button(frame_datos, text="Calcular", command=self.calcular_copago_evento, width=12)
        self.btn_calcular.grid(row=9, column=0, pady=6, padx=4)
        self.btn_registrar = ttk.Button(frame_datos, text="Registrar", command=self.registrar_usuario, width=12)
        self.btn_registrar.grid(row=9, column=1, pady=6, padx=4)
        self.btn_limpiar = ttk.Button(frame_datos, text="Limpiar", command=self.limpiar_campos, width=26)
        self.btn_limpiar.grid(row=10, column=0, columnspan=2, pady=4)

        # Sección de estructuras y listados (lado derecho)
        frame_struct = ttk.LabelFrame(self.frm_control, text="Estructuras de Datos", width=420)
        frame_struct.grid(row=0, column=1, padx=6, pady=6, sticky='n')

        ttk.Label(frame_struct, text="Seleccionar estructura:").grid(row=0, column=0, padx=4, pady=2, sticky='w')
        self.tipo_estructura = ttk.Combobox(frame_struct, values=["Pila", "Cola", "Lista"], state='readonly', width=12)
        self.tipo_estructura.grid(row=0, column=1, padx=4, pady=2, sticky='w')

        cols = ("id", "nombre", "edad", "estrato", "atencion", "valor")
        # Treeviews con columnas más estrechas para ajustar al tamaño
        self.tree_pila = ttk.Treeview(frame_struct, columns=cols, show='headings', height=6)
        self.tree_cola = ttk.Treeview(frame_struct, columns=cols, show='headings', height=6)
        self.tree_lista = ttk.Treeview(frame_struct, columns=cols, show='headings', height=6)

        for tree in (self.tree_pila, self.tree_cola, self.tree_lista):
            for col in cols:
                tree.heading(col, text=col.capitalize())
                tree.column(col, width=90, anchor='center')  # ancho reducido
        # Ubicar los treeviews en una sola fila con separación
        self.tree_pila.grid(row=1, column=0, padx=4, pady=4)
        self.tree_cola.grid(row=1, column=1, padx=4, pady=4)
        self.tree_lista.grid(row=1, column=2, padx=4, pady=4)

        # Botón para registrar en estructura
        self.btn_registrar_estructura = ttk.Button(self.frm_control, text="Registrar en Estructura", command=self.registrar_en_estructura, width=30)
        self.btn_registrar_estructura.grid(row=1, column=0, pady=6, padx=6, sticky='w')

        # Reporte (debajo)
        ttk.Label(self.frm_control, text="Reporte:").grid(row=2, column=0, sticky='w', padx=6, pady=2)
        self.reporte_text = tk.Text(self.frm_control, height=4, width=80, state='disabled')
        self.reporte_text.grid(row=3, column=0, columnspan=2, pady=4, padx=6)

        self.btn_reporte = ttk.Button(self.frm_control, text="Mostrar Reporte", command=self.mostrar_reporte, width=20)
        self.btn_reporte.grid(row=4, column=0, pady=6, padx=6, sticky='w')

    def limpiar_campos(self):
        self.tipo_id.set('')
        self.num_id.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.edad.delete(0, tk.END)
        self.estrato.set('')
        self.tipo_atencion.set('')
        self.fecha_registro.delete(0, tk.END)
        self.fecha_registro.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.valor_copago_var.set('')

    def calcular_copago_evento(self):
        try:
            estrato = int(self.estrato.get())
            atencion = self.tipo_atencion.get()
            valor = calcular_copago(estrato, atencion)
            self.valor_copago_var.set(str(valor))
        except:
            messagebox.showerror("Error", "Por favor, complete todos los campos y seleccione atención y estrato.")

    def registrar_usuario(self):
        # Validar campos
        if not all([self.tipo_id.get(), self.num_id.get(), self.nombre.get(), self.edad.get(),
                    self.estrato.get(), self.tipo_atencion.get(), self.valor_copago_var.get()]):
            messagebox.showerror("Error", "Complete todos los campos y calcule el copago.")
            return
        # Validar números
        try:
            int(self.num_id.get())
            int(self.edad.get())
        except:
            messagebox.showerror("Error", "El número ID y la edad deben ser números.")
            return
        # Validar nombre (permitir espacios)
        nombre_val = self.nombre.get().strip()
        if not nombre_val or not all(c.isalpha() or c.isspace() for c in nombre_val):
            messagebox.showerror("Error", "El nombre solo debe contener letras y espacios.")
            return
        # Crear objeto usuario
        usuario = EstructuraDatosUsuario(
            self.tipo_id.get(),
            self.num_id.get(),
            nombre_val,
            int(self.edad.get()),
            int(self.estrato.get()),
            self.tipo_atencion.get(),
            int(self.valor_copago_var.get()),
            self.fecha_registro.get()
        )
        # Agregar a estructura seleccionada (si no hay selección, pedir)
        estructura = self.tipo_estructura.get()
        if estructura == "Pila":
            self.pila.append(usuario)
        elif estructura == "Cola":
            self.cola.append(usuario)
        elif estructura == "Lista":
            self.lista.append(usuario)
        else:
            messagebox.showerror("Error", "Seleccione una estructura de datos.")
            return

        messagebox.showinfo("Registrado", "Usuario registrado correctamente.")
        self.limpiar_campos()
        self.actualizar_treeview()

    def registrar_en_estructura(self):
        estructura = self.tipo_estructura.get()
        if not estructura:
            messagebox.showerror("Error", "Seleccione una estructura de datos.")
            return
        # Llamar a registrar_usuario (ya añade a la estructura y actualiza el treeview)
        self.registrar_usuario()

    def actualizar_treeview(self):
        # Limpiar Treeviews
        for tree in [self.tree_pila, self.tree_cola, self.tree_lista]:
            for item in tree.get_children():
                tree.delete(item)
        # Agregar elementos
        for usuario in self.pila:
            self.tree_pila.insert('', 'end', values=(usuario.id_number, usuario.name, usuario.age, usuario.estrato, usuario.atencion, usuario.valor_copago))
        for usuario in self.cola:
            self.tree_cola.insert('', 'end', values=(usuario.id_number, usuario.name, usuario.age, usuario.estrato, usuario.atencion, usuario.valor_copago))
        for usuario in self.lista:
            self.tree_lista.insert('', 'end', values=(usuario.id_number, usuario.name, usuario.age, usuario.estrato, usuario.atencion, usuario.valor_copago))

    def mostrar_reporte(self):
        estructura = self.tipo_estructura.get()
        self.reporte_text.config(state='normal')
        self.reporte_text.delete('1.0', tk.END)
        if estructura == "Pila":
            suma_copagos = sum(usuario.valor_copago for usuario in self.pila)
            self.reporte_text.insert(tk.END, f"Total copago en Pila: ${suma_copagos}\n")
        elif estructura == "Cola":
            cantidad = len(self.cola)
            self.reporte_text.insert(tk.END, f"Cantidad registros en Cola: {cantidad}\n")
        elif estructura == "Lista":
            if len(self.lista) > 0:
                promedio = sum(usuario.age for usuario in self.lista) / len(self.lista)
                self.reporte_text.insert(tk.END, f"Promedio de edades en Lista: {promedio:.2f}\n")
            else:
                self.reporte_text.insert(tk.END, "No hay registros en Lista.\n")
        else:
            self.reporte_text.insert(tk.END, "Seleccione una estructura para reportar.\n")
        self.reporte_text.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()