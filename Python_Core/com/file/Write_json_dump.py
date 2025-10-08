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

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)