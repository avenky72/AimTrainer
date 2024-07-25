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
time = 3000
health = 10

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
    global time
    global points
    if points > 5 and len(targets) < 5:
        time = 2500
        if points > 10:
            time = 2000
            #create_target()
        if points > 15:
            time = 1750
            #create_target()
        if points > 20:
            time = 1500
            #create_target()
            #create_target()
        if points > 25:
            time = 1000
            #create_target()
            #create_target()
        if points > 30:
            time = 800
        if points > 40:
            time = 700
        if points > 50:
            time = 600
        if points > 60:
            time = 550
        if points > 70:
            time = 500
        if points > 80:
            time = 400
        if points > 90:
            time = 300
        if points == 100:
            print("You Win")
            return
            #create_target()
            #create_target()
            #create_target()
    print(time)
    root.after(time, create_target)


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
        '''if hit(t) == False:
            global health
            health += 1
        print("P: ", points, " H:", health)'''



create_target()


canvas.bind("<Button-1>", get_click_coordinates)

root.mainloop()
