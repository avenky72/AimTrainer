import tkinter as tk
import random


class AimTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("PC Aim Trainer by Atul Venky")
        self.canvas = tk.Canvas(root, width=800, height=800, bg="beige")
        self.canvas.pack()



if __name__ == "__main__":
    root = tk.Tk()

    game = AimTrainer(root)
    
    
    
    
    root.mainloop()