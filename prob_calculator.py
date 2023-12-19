import copy
import random

class Hat:
    def __init__(self, **balls):
        # Creates the list with the information of the balls that goes in the hat
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num_balls):
        # If the number of balls exceeds the quantity
        if num_balls >= len(self.contents):
            return self.contents
        
        # Get the random contents of the balls
        drawn_balls = random.sample(self.contents, num_balls)

        # Removes the balls that get random
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):

        # Create a copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)

        # Draw balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls match the expected balls
        success = all(drawn_balls.count(color) >= count for color, count in expected_balls.items())
        if success:
            successful_experiments += 1

    # Calculate the probability
    probability = successful_experiments / num_experiments
    return probability