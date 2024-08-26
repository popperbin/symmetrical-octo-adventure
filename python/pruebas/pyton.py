import tkinter as tk

# Clase para la ventana principal
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplicación con Tkinter")
        self.geometry("800x600")
        
        # Llamar a otra clase para crear un frame dentro de la ventana principal
        self.frame = CustomFrame(self)
        self.frame.pack(pady=20)
        
        # Botón para cerrar la aplicación
        self.close_button = tk.Button(self, text="Cerrar", command=self.quit)
        self.close_button.pack(pady=10)

# Clase personalizada para un frame
class CustomFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.label = tk.Label(self, text="¡Hola, Tkinter!")
        self.label.pack(padx=10, pady=10)
        
        self.button = tk.Button(self, text="Presionar", command=self.on_click)
        self.button.pack(padx=10, pady=10)
    
    def on_click(self):
        print("¡Botón presionado!")

# Función main
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()