capitals = {
    "USA": "Washinton D.C.",
    "India": "New Delhi",
    "China": "Beijin",
    "Rusia": "Moscow"
}

# Show the different attributes od the dictionary
# print(dir(capitals))

# Help function
# print(help(capitals))

print("********************")
# Show a value from the dictionary
print(capitals.get("USA"))
print(capitals["China"])

print("********************")
key="Rusia"
if capitals.get(key):
    cap = capitals.get(key)
    print(f"The capital exists: {cap}")
else:
    print("The capital does not exist")

print("********************")
# Update the dictionary
capitals.update({"Germany":"Berlin"})
print(capitals)

print("********************")
# Delete a key:value pair from the dictionary
capitals.pop("China")
print(capitals)

print("********************")
# Get all the keys from the dictionary without its values
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)


print("********************")
# Get all the values from the dictionary without its keys
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)


print("********************")
# items method for a dictionary

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")