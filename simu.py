from collections import defaultdict

class Robot:
    def __init__(self):
        self.platform = ['white', 'black']
        self.position = 0  # Start on the left side of the platform
        self.last_color = None
        self.last_move = None
        self.histograms = {
            ('white', 'left'): {'white': 1, 'black': 1},
            ('white', 'right'): {'white': 1, 'black': 1},
            ('black', 'left'): {'white': 1, 'black': 1},
            ('black', 'right'): {'white': 1, 'black': 1},
        }

    def move_left(self):
        if self.position > 0:
            self.histograms[(self.platform[self.position], 'left')][self.platform[self.position - 1]] += 1
            self.last_color = self.platform[self.position]
            self.last_move = 'left'
            self.position -= 1
        else:
            self.histograms[(self.platform[self.position], 'left')][self.platform[self.position]] += 1
            self.last_color = self.platform[self.position]
            self.last_move = 'left'
            print("The robot is already at the leftmost position.")

    def move_right(self):
        if self.position < len(self.platform) - 1:
            self.histograms[(self.platform[self.position], 'right')][self.platform[self.position + 1]] += 1
            self.last_color = self.platform[self.position]
            self.last_move = 'right'
            self.position += 1
        else:
            self.histograms[(self.platform[self.position], 'right')][self.platform[self.position]] += 1
            self.last_color = self.platform[self.position]
            self.last_move = 'right'
            print("The robot is already at the rightmost position.")

    def report_position(self):
        print(f"The robot is on the {self.platform[self.position]} side of the platform.")
        if self.last_color:
            print(f"The last color was {self.last_color}.")
        if self.last_move:
            print(f"The last move was {self.last_move}.")

    def calculate_probability(self, next_color, current_color, action):
        histogram = self.histograms[(current_color, action)]
        numerator = histogram[next_color]
        denominator = sum(histogram.values())
        return numerator / denominator if denominator != 0 else 0
    
    def print_histograms(self):
        for (current_color, action), histogram in self.histograms.items():
            print(f"Histogram for {current_color} tile + action {action}:")
            for next_color, count in histogram.items():
                print(f"  {next_color}: {count}")
# Usage
robot = Robot()
robot.move_right()
robot.move_left()
robot.move_left()
robot.move_right()
robot.move_right()
robot.move_left()
robot.move_right()
robot.move_left()
robot.move_left()
print(robot.calculate_probability('white', 'black', 'right'))  # P(st+1 = white|st = black, at = right)
robot.print_histograms()