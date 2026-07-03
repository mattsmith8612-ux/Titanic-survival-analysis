"""
Titanic Survival Analysis

This project explores the Titanic dataset using pandas and matplotlib.
The analysis investigates:
- passenger demographics
- missing values
- category frequencies
- survival rates across different groups
- the relationship between passenger class, gender and survival
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
)

# Basic exploration of the dataset
df.info()

# Determine how many missing values are present in each column
print(df.isna().sum())

# List of categorical variables to investigate
category_list = [
    "survived",
    "pclass",
    "sex",
    "embarked",
    "class",
    "who",
    "deck",
    "embark_town",
    "alive",
    "alone",
]


# Display the frequency of each category
for item in category_list:
    print(df[item].value_counts())

# Calculate the number of passengers in each ticket class
counts = df["pclass"].value_counts()


# Plot passenger frequencies by ticket class (vertical bar chart)
plt.figure()
plt.bar(counts.index, counts.values)
plt.title("Passenger Class Frequencies")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.show()

# Plot passenger frequencies by ticket class (horizontal bar chart)
plt.figure()
plt.barh(counts.index, counts.values)
plt.title("Passenger Class Frequencies")
plt.ylabel("Passenger Class")
plt.xlabel("Number of Passengers")
plt.show()


# Calculate survival rates for each categorical variable
for item in category_list[1:]:
    print(f"\nSurvival rates grouped by {item}:")
    print(df.groupby(item)["survived"].mean())

# Calculate survival rates by both passenger class and gender
print(df.groupby(["pclass", "sex"])["survived"].mean())


# Store survival rates by class and gender for visualisation
rates = df.groupby(["pclass", "sex"])["survived"].mean()


# Create readable labels for the plot
bar_labels = []
for item in rates.index:
    string_label = str(item[0]) + " - " + str(item[1].title())
    bar_labels.append(string_label)


# Visualise survival rates by passenger class and gender
plt.figure()
plt.barh(bar_labels, rates.values)
plt.title("Mean Passenger Survival Rate For Each Gender by Class")
plt.xlabel("Mean Passenger Survival Rate")
plt.ylabel("Passenger Gender and Class")
plt.show()
