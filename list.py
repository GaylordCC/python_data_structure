# List as a Array
cities = ["Barranquilla", "Medellin", "Bogota"]


#Print the element of with index 0
print(cities[0])

# Add a new city in the list
cities.append("Cali")

# Store the cities in an array
store_cities = []
for city in cities:
    print(city)
    store_cities.append(city)

print (store_cities)