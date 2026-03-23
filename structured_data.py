#import csv
"""
with open("test2/test.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age"])
    writer.writerow(["John","18"])

with open("test2/test.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open("test2/test.csv", "a", newline="") as f: #important to not forget newline, or else it will creat null values
    writer = csv.writer(f)
    writer.writerow(["Pedro", "20"])
    writer.writerow(["Lucas", "31"])
"""

#--------------------------------------#
import json
data = {"name": "John", "age": "18"}
#write
with open("test2/test2.json", "w") as f:
    json.dump(data, f)
#read
with open("test2/test2.json", "r") as f:
    data = json.load(f)
    print(data["name"])
