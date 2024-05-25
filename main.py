import tkinter as tk
from tkinter import ttk
import mysql.connector
import socket
from PIL import Image, ImageTk
from datetime import datetime  # Importa el módulo datetime para obtener la fecha y hora actual

class SQLQueryApp:
    def __init__(self, master):
        self.master = master
        master.title("SQL Query App")
        master.geometry("500x800")
        master.configure(bg="#f0f0f0")
        
        # Título en negrita
        self.title_label = tk.Label(master, text="SQL Query App", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)
    

        # Carga de la imagen
        self.image = Image.open("imagen.png")
        self.image = self.image.resize((50, 50), Image.LANCZOS)  # Redimensiona la imagen a 100x100 px
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Muestra la imagen en un widget Label
        self.image_label = tk.Label(master, image=self.photo, bg="#f0f0f0")
        self.image_label.pack(pady=10)

        # Entradas de texto y etiquetas
        self.ip_label = tk.Label(master, text="Dirección IP:", bg="#f0f0f0")
        self.ip_label.pack(pady=5)
        self.ip_entry = tk.Entry(master, width=50)
        self.ip_entry.insert(0, '127.0.0.1')  # IP local
        self.ip_entry.pack(pady=5)

        self.port_label = tk.Label(master, text="Puerto:", bg="#f0f0f0")
        self.port_label.pack(pady=5)
        self.port_entry = tk.Entry(master, width=50)
        self.port_entry.insert(0, '3306')  # Puerto por defecto de MySQL
        self.port_entry.pack(pady=5)

        self.user_label = tk.Label(master, text="Usuario:", bg="#f0f0f0")
        self.user_label.pack(pady=5)
        self.user_entry = tk.Entry(master, width=50)
        self.user_entry.insert(0, 'root')  # Usuario por defecto
        self.user_entry.pack(pady=5)

        self.password_label = tk.Label(master, text="Contraseña:", bg="#f0f0f0")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(master, width=50, show="*")
        self.password_entry.pack(pady=5)

        self.db_label = tk.Label(master, text="Nombre de la BD:", bg="#f0f0f0")
        self.db_label.pack(pady=5)
        self.db_entry = tk.Entry(master, width=50)
        self.db_entry.insert(0, 'test')
        self.db_entry.pack(pady=5)

        self.query_label = tk.Label(master, text="Sentencia SQL:", bg="#f0f0f0")
        self.query_label.pack(pady=5)
        self.query_entry = tk.Entry(master, width=50)
        #PREVIUSLY CREATED DE DB IN YOUR SYSTEM. CAN EXECUTE THIS LINE:
        self.query_entry.insert(0,'CREATE TABLE ITSELISA (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT);')  # Consulta por defecto
        #LATER, U CAN DESTROY THE TABLE.
        #self.query_entry.insert(0,'DROP TABLE ITSELISA;')  # Consulta por defecto
        self.query_entry.pack(pady=5)

        # Botón de ejecución
        self.run_button = tk.Button(master, text="Ejecutar Consulta", command=self.run_query)
        self.run_button.pack(pady=10)

        # Área de resultados
        self.result_text = tk.Text(master, wrap="word", height=15)
        self.result_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.result_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=self.scrollbar.set)

    def run_query(self):
        ip_address = self.ip_entry.get()
        port = int(self.port_entry.get())
        user = self.user_entry.get()
        password = self.password_entry.get()
        database = self.db_entry.get()
        query = self.query_entry.get()
        
        try:
            conn = mysql.connector.connect(
                host=ip_address,
                port=port,
                user=user,
                password=password,
                database=database  # Especificar la base de datos aquí
            )
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                self.result_text.insert(tk.END, f"{row}\n")
            conn.close()
            
            # Ahora intentaremos conectar a la dirección IP y puerto especificados
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                self.result_text.insert(tk.END, f"\nConexión exitosa a {ip_address}:{port}\n")
            else:
                self.result_text.insert(tk.END, f"\nError al conectar a {ip_address}:{port}\n")
            sock.close()
            
        except Exception as e:
            self.result_text.insert(tk.END, f"Error al ejecutar la consulta o conectar al puerto: {e}\n")

def main():
    root = tk.Tk()
    app = SQLQueryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
