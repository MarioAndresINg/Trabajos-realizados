# Fase4MarioGaravito.py
# Aplicación: Fase4MarioGaravito
# Requerimientos: Python 3.x, Tkinter (viene con Python)

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from datetime import datetime
import math

# --------------------------
# Estructura de datos: Nodo
# --------------------------
class Node:
    def __init__(self, value, level=1):
        self.value = value
        self.left = None
        self.right = None
        self.level = level  

# --------------------------
# Árbol Binario de Búsqueda
# --------------------------
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserta value en el árbol. Devuelve (True, '') si se inserta,
        o (False, mensaje_error) si no."""
        if self.root is None:
            self.root = Node(value, level=1)
            return True, ''
        # recorrer para insertar y calcular nivel
        current = self.root
        while True:
            if value == current.value:
                return False, 'El valor ya existe en el árbol.'
            elif value < current.value:
                if current.left:
                    current = current.left
                else:
                    new_level = current.level + 1
                    if new_level > 4:
                        return False, 'No es posible insertar: excede el nivel máximo permitido (4).'
                    current.left = Node(value, level=new_level)
                    return True, ''
            else:  # value > current.value
                if current.right:
                    current = current.right
                else:
                    new_level = current.level + 1
                    if new_level > 4:
                        return False, 'No es posible insertar: excede el nivel máximo permitido (4).'
                    current.right = Node(value, level=new_level)
                    return True, ''

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def clear(self):
        self.root = None

    # Recorridos
    def inorder(self, node=None, acc=None):
        if acc is None:
            acc = []
        if node is None:
            node = self.root
        if node is None:
            return acc
        if node.left:
            self.inorder(node.left, acc)
        acc.append(node.value)
        if node.right:
            self.inorder(node.right, acc)
        return acc

    def preorder(self, node=None, acc=None):
        if acc is None:
            acc = []
        if node is None:
            node = self.root
        if node is None:
            return acc
        acc.append(node.value)
        if node.left:
            self.preorder(node.left, acc)
        if node.right:
            self.preorder(node.right, acc)
        return acc

    def postorder(self, node=None, acc=None):
        if acc is None:
            acc = []
        if node is None:
            node = self.root
        if node is None:
            return acc
        if node.left:
            self.postorder(node.left, acc)
        if node.right:
            self.postorder(node.right, acc)
        acc.append(node.value)
        return acc

    # para dibujo: calcular lista de nodos en inorder con referencias para posicion
    def nodes_inorder_with_refs(self):
        res = []
        def helper(n):
            if n is None:
                return
            helper(n.left)
            res.append(n)
            helper(n.right)
        helper(self.root)
        return res

# --------------------------
# Interfaz gráfica con Tkinter
# --------------------------
class ArbolApp:
    def __init__(self, master, student_name=""):
        self.master = master
        master.title("Fase4MarioGaravito")
        self.student_name = student_name or "Estudiante"
        self.bst = BinarySearchTree()
        self._build_login()

    def _build_login(self):
        self.login_frame = ttk.Frame(self.master, padding=20)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        lbl_title = ttk.Label(self.login_frame, text="Aplicacion:  Arboles Binarios",)
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0,10))

        lbl_name = ttk.Label(self.login_frame, text=f"Nombre del estudiante: {self.student_name}")
        lbl_name.grid(row=1, column=0, columnspan=2, sticky="w")
        lbl_date = ttk.Label(self.login_frame, text=f"Fecha: {datetime.now().strftime('%d-%m-%Y')}")
        lbl_date.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0,10))

        ttk.Label(self.login_frame, text="Contraseña:").grid(row=3, column=0, sticky="e")
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=3, column=1, sticky="w")
        btn_login = ttk.Button(self.login_frame, text="Ingresar", command=self._validate_login)
        btn_login.grid(row=4, column=0, columnspan=2, pady=(10,0))

        # hint (oculto si no quieres mostrarlo)
        hint = ttk.Label(self.login_frame, text="(La contraseña genérica es 'UNAD')", font=("Arial", 8))
        hint.grid(row=5, column=0, columnspan=2, pady=(8,0))

    def _validate_login(self):
        pwd = self.password_entry.get().strip()
        if pwd == "UNAD":
            # abrir ventana principal
            self.login_frame.destroy()
            self._build_main_window()
        else:
            messagebox.showerror("Acceso denegado", "Contraseña incorrecta. Intente de nuevo.")

    def _build_main_window(self):
        self.master.title(" Árbol Binario de Búsqueda")
        # layout principal: izquierda canvas (árbol), derecha paneles de recorrido y controles
        main = ttk.Frame(self.master, padding=8)
        main.grid(row=0, column=0, sticky="nsew")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # Canvas para dibujo del árbol
        canvas_frame = ttk.LabelFrame(main, text="Árbol", padding=6)
        canvas_frame.grid(row=0, column=0, rowspan=4, sticky="nsew", padx=(0,8), pady=(0,8))
        canvas_frame.rowconfigure(0, weight=1)
        canvas_frame.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(canvas_frame, width=700, height=400, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Panel de controles
        controls = ttk.LabelFrame(main, text="Controles", padding=8)
        controls.grid(row=0, column=1, sticky="ew", pady=(0,8))
        ttk.Label(controls, text="Valor (entero):").grid(row=0, column=0, sticky="w")
        self.value_entry = ttk.Entry(controls)
        self.value_entry.grid(row=0, column=1, sticky="w")
        btn_add = ttk.Button(controls, text="Agregar Nodo", command=self.on_add)
        btn_add.grid(row=1, column=0, pady=(6,0))
        btn_search = ttk.Button(controls, text="Buscar Nodo", command=self.on_search)
        btn_search.grid(row=1, column=1, pady=(6,0))
        btn_clear = ttk.Button(controls, text="Limpiar", command=self.on_clear)
        btn_clear.grid(row=2, column=0, pady=(6,0))
        btn_exit = ttk.Button(controls, text="Salir", command=self.master.quit)
        btn_exit.grid(row=2, column=1, pady=(6,0))
 
        # Paneles de recorrido
        pre_frame = ttk.LabelFrame(main, text="Preorden", padding=6)
        pre_frame.grid(row=1, column=1, sticky="ew", pady=(6,0))
        self.pre_text = tk.Text(pre_frame, width=30, height=4, state="disabled")
        self.pre_text.grid(row=0, column=0)

        in_frame = ttk.LabelFrame(main, text="Inorden", padding=6)
        in_frame.grid(row=2, column=1, sticky="ew", pady=(6,0))
        self.in_text = tk.Text(in_frame, width=30, height=4, state="disabled")
        self.in_text.grid(row=0, column=0)

        post_frame = ttk.LabelFrame(main, text="Posorden", padding=6)
        post_frame.grid(row=3, column=1, sticky="ew", pady=(6,0))
        self.post_text = tk.Text(post_frame, width=30, height=4, state="disabled")
        self.post_text.grid(row=0, column=0)

        # configurar grid para expandir canvas
        main.rowconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)

        # Mapa para posiciones de nodos: {node: (x,y,oval_id,text_id,line_ids)}
        self.node_draw_map = {}
        self.draw_tree()  # dibujo vacío inicial

    # ----------------------------------------------------------
    # Handlers: agregar, buscar, limpiar
    # ----------------------------------------------------------
    def on_add(self):
        val = self.value_entry.get().strip()
        if not val:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese un número entero.")
            return
        try:
            num = int(val)
        except ValueError:
            messagebox.showerror("Entrada inválida", "Solo se permiten valores enteros.")
            return
        ok, msg = self.bst.insert(num)
        if not ok:
            messagebox.showerror("No se pudo insertar", msg)
            return
        # reiniciar entrada y actualizar gráficas y recorridos
        self.value_entry.delete(0, tk.END)
        self.draw_tree()
        self.update_traversals()

    def on_search(self):
        val = self.value_entry.get().strip()
        if not val:
            messagebox.showwarning("Entrada vacía", "Ingrese el valor a buscar.")
            return
        try:
            num = int(val)
        except ValueError:
            messagebox.showerror("Entrada inválida", "Solo se permiten valores enteros.")
            return
        found_node = self.bst.search(num)
        if not found_node:
            messagebox.showinfo("Buscar Nodo", f"El nodo {num} NO existe en el árbol.")
            return
        # resaltar nodo encontrado en el canvas (por ejemplo, con doble borde)
        self.draw_tree(highlight_value=num)
        messagebox.showinfo("Buscar Nodo", f"El nodo {num} existe en el árbol (nivel {found_node.level}).")

    def on_clear(self):
        if messagebox.askyesno("Limpiar", "¿Desea limpiar todo el árbol?"):
            self.bst.clear()
            self.node_draw_map.clear()
            self.draw_tree()
            self.update_traversals()

    # ----------------------------------------------------------
    # Dibujo del árbol en Canvas
    # ----------------------------------------------------------
    def draw_tree(self, highlight_value=None):
        self.canvas.delete("all")
        root = self.bst.root
        if root is None:
            # texto indicando árbol vacío
            self.canvas.create_text(350, 200, text="Árbol vacío. Inserte nodos.", font=("Arial", 14))
            return

        # obtener nodos en inorder para asignar x
        inorder_nodes = self.bst.nodes_inorder_with_refs()
        n = len(inorder_nodes)
        if n == 0:
            return

        # asignar x en función del índice inorder
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])
        margin_x = 40
        usable_w = width - 2*margin_x
        # evitar división por cero
        if n == 1:
            spacing_x = 0
        else:
            spacing_x = usable_w / (n - 1)

        # mapa de nodo->x (por referencia de objeto)
        node_to_x = {}
        for idx, node in enumerate(inorder_nodes):
            x = margin_x + idx * spacing_x
            node_to_x[node] = x

        # dibujar líneas y nodos con recorrido por niveles
        def draw_node(nodo):
            x = node_to_x[nodo]
            y = 30 + (nodo.level - 1) * 80  # separar niveles verticalmente (nivel 1 en y=30)
            r = 18  # radio de los nodos
            # dibujar enlaces a hijos
            if nodo.left:
                x_left = node_to_x[nodo.left]
                y_left = 30 + (nodo.left.level - 1) * 80
                self.canvas.create_line(x, y + r, x_left, y_left - r, width=2)
            if nodo.right:
                x_right = node_to_x[nodo.right]
                y_right = 30 + (nodo.right.level - 1) * 80
                self.canvas.create_line(x, y + r, x_right, y_right - r, width=2)

            # dibujar el nodo (círculo)
            if highlight_value is not None and nodo.value == highlight_value:
                oval = self.canvas.create_oval(x - r - 4, y - r - 4, x + r + 4, y + r + 4, width=3)
            else:
                oval = None
            circle = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="white")
            text_id = self.canvas.create_text(x, y, text=str(nodo.value), font=("Arial", 10, "bold"))
            # almacenar referencias opcionales
            self.node_draw_map[nodo] = (x, y, circle, text_id, oval)

            # dibujar hijos recursivamente
            if nodo.left:
                draw_node(nodo.left)
            if nodo.right:
                draw_node(nodo.right)

        # dibujar a partir de la raíz
        draw_node(root)

        # si hay nodos con nivel > 4 (no deberían), mostrarlos con advertencia
        max_level_found = self._max_level(self.bst.root)
        if max_level_found > 4:
            messagebox.showwarning("Nivel máximo excedido", "El árbol contiene nodos por encima del nivel 4.")

    def _max_level(self, node):
        if not node:
            return 0
        return max(node.level, self._max_level(node.left), self._max_level(node.right))

    # ----------------------------------------------------------
    # Actualizar paneles de recorridos
    # ----------------------------------------------------------
    def update_traversals(self):
        pre = self.bst.preorder()
        ino = self.bst.inorder()
        post = self.bst.postorder()
        self._set_text(self.pre_text, " - ".join(map(str, pre)))
        self._set_text(self.in_text, " - ".join(map(str, ino)))
        self._set_text(self.post_text, " - ".join(map(str, post)))

    def _set_text(self, widget, text):
        widget.config(state="normal")
        widget.delete(1.0, tk.END)
        widget.insert(tk.END, text)
        widget.config(state="disabled")


# --------------------------
# Ejecutar la aplicación
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ArbolApp(root, student_name="Mario Andrés Garavito")
    root.mainloop()
