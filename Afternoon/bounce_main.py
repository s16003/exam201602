from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 238, 475)

        starts = [-3, -2, -1,1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = abs(self.y)

        if pos[3] >= self.canvas_height:
            # self.y = abs(self.y) * -1
            self.hit_bottom = True

        if pos[0] <= 0:
            self.x = abs(self.x) * 1

        if pos[2] >= self.canvas_width:
            self.x = abs(self.x) *-1

        if self.hit_paddle(pos):
            self.y = abs(self.x) * random.choice((-2, -3, -4))

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 110, 10, fill=color)
        self.canvas.move(self.id, 200, 500)

        self.x = 0
        self.y = 0

        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        self.started = False

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)
        self.canvas.bind_all('<Shift-Right>', self.start_game)
        self.canvas.bind_all('<Shift-Left>', self.start_game)
        self.canvas.bind_all('<Shift-Up>', self.start_game)
        self.canvas.bind_all('<Shift-Down>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0

        elif pos[2] >= self.canvas_width:
            self.x = 0

        if pos[1] <= 0:
            self.y = 0

        elif pos[3] >= self.canvas_height:
            self.y = 0

    def turn_left(self, event):
        self.x = -4

    def turn_right(self, event):
        self.x = 4

    def turn_up(self, event):
        self.y = -1.5

    def turn_down(self, event):
        self.y = 1.5

    def start_game(self, event):
        self.started = True

tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
c = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
c.pack()
tk.update()


p = Paddle(c, 'green')
ball = Ball(c, p, 'red')
game_over_text = c.create_text(250, 200, text='GAME OVER', state='hidden')
Discription = c.create_text(265, 590, text='start : Shift + Any cursor          operation : ↑ ↓ ← →', state='normal')

def update():
    if not ball.hit_bottom and p.started == True:
        ball.draw()
        p.draw()

    if not ball.hit_bottom == False:
        time.sleep(1)
        c.itemconfig(game_over_text, state='normal')

    tk.update_idletasks()
    tk.update()
    tk.after(10,update)

tk.after(10,update)
tk.mainloop()
