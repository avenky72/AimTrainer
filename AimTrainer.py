import tkinter as tk
import random
import math


root = tk.Tk()
root.title("Aim Trainer")
canvas = tk.Canvas(root, width=800, height=800, bg="beige")
canvas.pack()
#global points
points = 0
targets = {}
r = 50

# Periodically add target
def create_target():
    # Random color 
    def randColor():
        return f'#{random.randint(0, 0xFFFFFF):06x}'

    x = random.randint(100, 700)
    y = random.randint(100, 700)
    color = randColor()
    target = canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)
    targets[target] = {'x': x, 'y': y, 'r': r}
    print(targets)


# Remove target after 3 seconds
def remove_target(target):
    if target in targets:
        canvas.delete(target)
        del targets[target]

def get_click_coordinates(event):
    a, b = event.x, event.y
    
    # If the target is clicked via MouseClick, increase the point total and remove target
    def hit(target):
        hit_target = targets[target]
        target_x, target_y, radius = hit_target['x'], hit_target['y'], hit_target['r']
        in_target = math.sqrt((a - target_x) ** 2 + (b - target_y) ** 2)
        return in_target <= radius

    for t in targets:
        if hit(t):
            global points
            points += 1
            print(points)
            remove_target(t)
            if not targets:
                break



create_target()
create_target()
create_target()
create_target()

canvas.bind("<Button-1>", get_click_coordinates)

root.mainloop()
