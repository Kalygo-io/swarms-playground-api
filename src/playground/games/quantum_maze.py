import random
import time
import os

class QuantumMaze:
    def __init__(self, size=5):
        self.size = size
        self.maze = self.generate_maze()
        self.player_pos = [0, 0]
        self.exit_pos = [size - 1, size - 1]
        self.game_over = False

    def generate_maze(self):
        return [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def display_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] == self.player_pos:
                    print('P', end=' ')
                elif [i, j] == self.exit_pos:
                    print('E', end=' ')
                else:
                    print(self.maze[i][j], end=' ')
            print()
        print("Use WASD to move. Reach 'E' to exit.")

    def move_player(self, direction):
        if direction == 'w' and self.player_pos[0] > 0:
            self.player_pos[0] -= 1
        elif direction == 's' and self.player_pos[0] < self.size - 1:
            self.player_pos[0] += 1
        elif direction == 'a' and self.player_pos[1] > 0:
            self.player_pos[1] -= 1
        elif direction == 'd' and self.player_pos[1] < self.size - 1:
            self.player_pos[1] += 1

    def shift_maze(self):
        # Randomly shift the maze
        for _ in range(random.randint(1, 3)):
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up' and self.player_pos[0] > 0:
                self.player_pos[0] -= 1
            elif direction == 'down' and self.player_pos[0] < self.size - 1:
                self.player_pos[0] += 1
            elif direction == 'left' and self.player_pos[1] > 0:
                self.player_pos[1] -= 1
            elif direction == 'right' and self.player_pos[1] < self.size - 1:
                self.player_pos[1] += 1

    def play(self):
        print("Welcome to QuantumMaze!")
        while not self.game_over:
            self.display_maze()
            move = input("Your move (WASD): ").lower()
            if move in ['w', 'a', 's', 'd']:
                self.move_player(move)
                if self.player_pos == self.exit_pos:
                    self.game_over = True
                    print("Congratulations! You've exited the maze!")
                self.shift_maze()
            else:
                print("Invalid move! Use W, A, S, or D.")

if __name__ == "__main__":
    game = QuantumMaze()
    game.play()