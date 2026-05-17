import csv

print("--- Writing to a CSV file ---")
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 24, "London"],
    ["Charlie", 35, "Paris"],
]

# 'newline=""' is crucial when writing CSVs to prevent extra blank rows
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)  # Creates a writer object
    writer.writerows(data)  # Writes multiple rows from a list of lists
print("Data written to people.csv.")

# Reading from a CSV file
print("\n--- Reading from a CSV file (as lists of strings) ---")
with open("people.csv", "r") as file:
    reader = csv.reader(file)  # Creates a reader object
    for row in reader:
        print(row)
# Expected Output:
# ['Name', 'Age', 'City']
# ['Alice', '30', 'New York']
# ['Bob', '24', 'London']
# ['Charlie', '35', 'Paris']

# Reading from a CSV file as dictionaries (more convenient for column-based access)
print("\n--- Reading from a CSV file (as dictionaries) ---")
with open("people.csv", "r") as file:
    reader = csv.DictReader(
        file
    )  # The first row is automatically used as keys for dictionaries
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}")
