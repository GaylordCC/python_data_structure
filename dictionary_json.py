import json

# Dictionary
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Bogotá"
}

# Convert the dictionary to JSON
mi_json = json.dumps(mi_diccionario)
print(mi_json)

# Convert a JSON to a dictionary
mi_diccionario_de_json = json.loads(mi_json)
print(mi_diccionario_de_json["nombre"])