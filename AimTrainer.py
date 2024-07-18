import tkinter as tk
import random


class AimTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("PC Aim Trainer by Atul Venky")
        self.canvas = tk.Canvas(root, width=800, height=800, bg="beige")
        self.canvas.pack()

    # Periodically add target
    def create_target():
        return None

    # Remove target after 3 seconds
    def remove_target():
        return None
    
    # If the target is clicked via MouseClick, increase the point total and remove target
    def hit():
        return None


if __name__ == "__main__":
    root = tk.Tk()

    game = AimTrainer(root)
    
    
    
    
    root.mainloop()