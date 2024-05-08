from collections import defaultdict
import random
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
            #print("The robot is already at the leftmost position.")

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
            #print("The robot is already at the rightmost position.")

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

    def choose_action(self, current_color):
        # Calculate probabilities for both actions
        prob_left = self.calculate_probability('white', current_color, 'left')
        prob_right = self.calculate_probability('white', current_color, 'right')

        # Choose action with higher probability, or randomly if probabilities are equal
        if prob_left > prob_right:
            return 'left'
        elif prob_right > prob_left:
            return 'right'
        else:
            return random.choice(['left', 'right'])
# Test the Robot class
robot = Robot()
for i in range(10):
    current_color = robot.platform[robot.position]
    action = robot.choose_action(current_color)
    if action == 'left':
        robot.move_left()
    else:
        robot.move_right()

print(robot.calculate_probability('white', 'black', 'right'))  # P(st+1 = white|st = black, at = right)
robot.print_histograms()