import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


filename = "data.json"
person = Person("John Doe", 30)

# __dict__ produces a dictionary object
json_data = json.dumps(person.__dict__)

# Open the file in write mode
with open(filename, "w") as file:
    json.dump(json_data, file)


# Open the file in read mode
with open(filename, "r") as file:
    json_content = json.load(file)

print(json_content)
