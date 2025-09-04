import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("height_age.csv")
ages = data["age (years)"]
heights = data["height (cm)"]

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(ages, heights, color='blue', alpha=0.6, edgecolors='w', s=100)
plt.title("Child Height vs Age")

plt.xlabel("Age (years)")
plt.ylabel("Height (cm)")
plt.grid(True)
plt.savefig("height_age_plot.png")
