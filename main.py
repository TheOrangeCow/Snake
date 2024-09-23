import tkinter as tk
import random


WIDTH = 400
HEIGHT = 400
DELAY = 100 

class SnakeGame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.spawn_food()
        self.score = 0
        self.bind("<Up>", self.change_direction)
        self.bind("<Down>", self.change_direction)
        self.bind("<Left>", self.change_direction)
        self.bind("<Right>", self.change_direction)
        self.game_loop()
    
    def spawn_food(self):
        x = random.randint(1, (WIDTH - 10) // 10) * 10
        y = random.randint(1, (HEIGHT - 10) // 10) * 10
        return (x, y)
    
    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x+10, y+10, fill="white", tag="snake")
    
    def draw_food(self):
        x, y = self.food
        self.canvas.create_oval(x, y, x+10, y+10, fill="red", tag="food")
    
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 10)
        elif self.direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 10, head_y)
        self.snake = [new_head] + self.snake[:-1]
    
    def check_collision(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True
        if self.snake[0] in self.snake[1:]:
            return True
        return False
    
    def check_food(self):
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.canvas.delete("food")
            self.food = self.spawn_food()
            self.score += 1
            self.title("Snake - Score: {}".format(self.score))
    
    def change_direction(self, event):
        new_direction = event.keysym
        if new_direction in ["Up", "Down", "Left", "Right"]:
            if new_direction == "Up" and self.direction != "Down":
                self.direction = new_direction
            elif new_direction == "Down" and self.direction != "Up":
                self.direction = new_direction
            elif new_direction == "Left" and self.direction != "Right":
                self.direction = new_direction
            elif new_direction == "Right" and self.direction != "Left":
                self.direction = new_direction
    
    def game_loop(self):
        if self.check_collision():
            self.game_over()
            return
        self.move_snake()
        self.check_food()
        self.draw_snake()
        self.draw_food()
        self.after(DELAY, self.game_loop)
    
    def game_over(self):
        self.title("Snake - Game Over! Score: {}".format(self.score))


game = SnakeGame()
game.title("Snake")
game.mainloop()

