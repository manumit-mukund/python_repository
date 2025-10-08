import json
import os

os.getcwd()
os.chdir(r"../../resources")

# Data to be written
dictionary = {
    "name": "Manu",
    "rollno": 2,
    "cgpa": 6,
    "phonenumber": "123"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample1.json", "w") as outfile:
    outfile.write(json_object)