import tkinter as tk

class comandos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.label = tk.Label(self, text="¡Hola, let's jam!")
        self.label.pack(padx=10, pady=10)
        
        self.button = tk.Button(self, text="Presionar", command=self.on_click)
        self.button.pack(padx=10, pady=10)
    
    def on_click(self):
        print("¡Botón presionado!")
