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

        print(f"Last state: {self.last_color}, Action taken: {self.last_move}, Result color: {self.platform[self.position]}")
        print(f"|-----------------|")
        print(f"|  BOT  ||        |")
        print(f"| White || Black  |")
        print(f"****************************************************************************")
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
        print(f"Last state: {self.last_color}, Action taken: {self.last_move}, Result color: {self.platform[self.position]}")
        print(f"|-----------------|")
        print(f"|       ||   BOT  |")
        print(f"| White || Black  |")
        print(f"****************************************************************************")


    def report_position(self):
        print(f"The robot is on the {self.platform[self.position]} side of the platform.")
        if self.last_color:
            print(f"The last color was {self.last_color}.")
        if self.last_move:
            print(f"The last move was {self.last_move}.")
    
    def print_histograms(self):
        for (current_color, action), histogram in self.histograms.items():
            print(f"Histogram for {current_color} tile + action {action}:")
            for next_color, count in histogram.items():
                print(f"  {next_color}: {count}")

    def choose_action(self, current_color):
        # Get counts for both colors for both actions
        count_left_white = self.histograms[(current_color, 'left')]['white']
        count_right_white = self.histograms[(current_color, 'right')]['white']
        count_left_black = self.histograms[(current_color, 'left')]['black']
        count_right_black = self.histograms[(current_color, 'right')]['black']

        # Determine the color with the highest count and its corresponding action
        max_count = max(count_left_white, count_right_white, count_left_black, count_right_black)
        if (count_left_white + count_right_white) == (count_left_black + count_right_black):
            return random.choice(['left', 'right'])
        elif max_count == count_left_white or max_count == count_left_black:
            return 'left'
        elif max_count == count_right_white or max_count == count_right_black:
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

robot.print_histograms()