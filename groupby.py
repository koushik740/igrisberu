import numpy as np
import pandas as pd
# Part (a): Represent the data in a 10x2 array
data = np.array([
    [1, 6012],
    [2, 4079],
    [3, 6386],
    [4, 5230],
    [5, 4598],
    [6, 5564],
    [7, 6971],
    [8, 7763],
    [9, 8032],
    [10, 8569]
])
# Part (b): Add 2000 steps for each day
data[:, 1] += 2000  # Add 2000 to all entries in the second column
# Part (c): Print an array containing steps walked in sorted order
sorted_steps = np.sort(data[:, 1])  # Sort the steps
print("Sorted steps walked:", sorted_steps)
# Part (d): Add 1000 steps to all observations using Pandas
df = pd.DataFrame(data, columns=['Day', 'Steps'])
df['Steps'] += 1000  # Add 1000 steps to each day's steps
# Part (e): Find out the days on which he walked more than 7000 steps
days_more_than_7000 = df[df['Steps'] > 7000]  # Filter the days with steps > 7000
# Display the results
print("Data with additional 2000 steps:\n", data)
print("Data after adding 1000 steps using Pandas:\n", df)
print("Days with more than 7000 steps:\n", days_more_than_7000)
