import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

class Snake:
    def __init__(self, x_cords, y_cords, x_size, y_size, obstacles, animation, direction):
        self.x_cords = x_cords
        self.y_cords = y_cords
        self.x_size = x_size
        self.y_size = y_size
        # przeszkody
        self.obstacles = obstacles
        # animacja w wężu
        self.animation = animation
        # kierunek węża
        self.direction = direction

    def move(self):
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        # wyłączamy taką możliwość że wąż zawróci i przez to się ze sobą zderzy
        new_dir = random.choice([m for m in moves if m[0] != -1 * self.direction[0] and m[1] != -1 * self.direction[1]])
        # print(f"prev dir: {self.direction}")
        # print(f"new dir: {new_dir}")
        # print('=================')
        self.direction = new_dir
        head_x = self.x_cords[0]
        head_y = self.y_cords[0] 
        tail_x = self.x_cords[:-1]
        tail_y = self.y_cords[:-1]
        new_head_x = (head_x + new_dir[0]) % (self.x_size + 1)
        new_head_y = (head_y + new_dir[1]) % (self.y_size + 1)
        # sprawdzenie kolizji z segmentem
        self.hitTail(new_head_x, new_head_y)
        # sprawdzenie kolizji z blokami
        self.hitObstacle(new_head_x, new_head_y)

        tail_x.insert(0, new_head_x)
        tail_y.insert(0, new_head_y)
        self.x_cords = tail_x
        self.y_cords = tail_y



    # def draw(self, frame):
    #     self.move()
    #     plt.scatter(self.x_cords, self.y_cords, color='green', marker='o', s=100)
    #     plt.scatter(self.x_cords[0], self.y_cords[0], color='red', marker='o', s=100)
    def hitTail(self, new_head_x,new_head_y):
        # sprawdzenie czy nowa głowa nie będzie w ogonie
        if (new_head_x,new_head_y) in zip(self.x_cords,self.y_cords):
            self.animation.event_source.stop()
            print("Game over - own collision")

    # sprawdzenie kwadratu, nie tylko środkowej współrzędnej, ale całego obrysu
    def hitObstacle(self, new_head_x, new_head_y):
        head_size = 0.5
        for pair in self.obstacles:
            size = 0.75
            if (
            (pair[0] - size) <= new_head_x + head_size
                and (pair[0] + size) >= new_head_x - head_size
                and (pair[1] - size) <= new_head_y + head_size
                and (pair[1] + size) >= new_head_y - head_size
            ):
                
                self.animation.event_source.stop()
                print("hitObstacle")



class Obstacles:
    def __init__(self, x_cords, y_cords, size):
        self.x_cords = x_cords
        self.y_cords = y_cords
        self.size = size

    def draw(self, frame):
        for i in range(len(self.x_cords)):
            plt.scatter(self.x_cords[i], self.y_cords[i], marker='s', color='black', s=self.size)

class Game:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.fig, self.ax = plt.subplots()
        # wybór koordynatów dla przeszkód
        obstacles_x = [(random.random() * 10) % self.x_size for _ in range(1,10)]
        obstacles_y = [(random.random() * 10) % self.y_size for _ in range(1,10)]
        self.obstacles = Obstacles(obstacles_x, obstacles_y, 1000)

        snake_x,snake_y = [1,1,1],[1,1.2,1.3]

        # animation setup
        self.animation = FuncAnimation(self.fig, self.update, interval=400)

        self.snake = Snake(snake_x, snake_y, x_size, y_size, zip(obstacles_x, obstacles_y), self.animation, (1,0))
        
        # narysowanie wykresów
        self.tail_scatter = self.ax.scatter(self.snake.x_cords, self.snake.y_cords, color='green', marker='o', s=100)
        # inne pokolorowanie głowy
        self.head_scatter = self.ax.scatter(self.snake.x_cords[0], self.snake.y_cords[0], color='red', marker='o',
                                            s=100)
        

    def update(self, frame):
        self.ax.clear()
        self.obstacles.draw(frame)
        self.snake.move()

        self.tail_scatter = self.ax.scatter(self.snake.x_cords, self.snake.y_cords, color='green', marker='o', s=100)
        self.head_scatter = self.ax.scatter(self.snake.x_cords[0], self.snake.y_cords[0], color='red', marker='o', s=100)

        self.ax.set_xlim(0, self.x_size)
        self.ax.set_ylim(0, self.y_size)
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.set_title('Snake Game')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game(5, 5)
    plt.show()