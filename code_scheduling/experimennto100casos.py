import random
import csv
from ActivitySelector import Greedy
from ActivitySelector import DynamicProgramming

def generate_random_activities(nAct, nSlots):
    activities = []
    s = 0
    while s <= nAct:
        start = random.randint(0, nSlots - 1)
        end = random.randint(start + 1, nSlots)
        if start < end:
            activities.append(("act_%d" % s, start, end))
            s = s + 1
    return activities

# Prepare the CSV file
with open('results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test Run", "Greedy Result", "Dynamic Programming Result"])

    # Run the entire process 100 times
    for i in range(1, 101):
        # Generate random activities
        activities = generate_random_activities(100, 50)  # Adjust the numbers as needed

        # Run the algorithms
        greedy_results = len(Greedy(activities))  # Count the number of activities
        dp_results = DynamicProgramming(activities)

        # Write the results to the CSV file
        writer.writerow([i, greedy_results, dp_results])