import time

bienvenido = r"""
  _______   ______  ________  __    __  __     __  ________  __    __  ______  _______    ______  
 |       \ |      \|        \|  \  |  \|  \   |  \|        \|  \  |  \|      \|       \  /      \ 
 | $$$$$$$\ \$$$$$$| $$$$$$$$| $$\ | $$| $$   | $$| $$$$$$$$| $$\ | $$ \$$$$$$| $$$$$$$\|  $$$$$$\
 | $$__/ $$  | $$  | $$__    | $$$\| $$| $$   | $$| $$__    | $$$\| $$  | $$  | $$  | $$| $$  | $$
 | $$    $$  | $$  | $$  \   | $$$$\ $$ \$$\ /  $$| $$  \   | $$$$\ $$  | $$  | $$  | $$| $$  | $$
 | $$$$$$$\  | $$  | $$$$$   | $$\$$ $$  \$$\  $$ | $$$$$   | $$\$$ $$  | $$  | $$  | $$| $$  | $$
 | $$__/ $$ _| $$_ | $$_____ | $$ \$$$$   \$$ $$  | $$_____ | $$ \$$$$ _| $$_ | $$__/ $$| $$__/ $$
 | $$    $$|   $$ \| $$     \| $$  \$$$    \$$$   | $$     \| $$  \$$$|   $$ \| $$    $$ \$$    $$
  \$$$$$$$  \$$$$$$ \$$$$$$$$ \$$   \$$     \$     \$$$$$$$$ \$$   \$$ \$$$$$$ \$$$$$$$   \$$$$$$ 
"""

print(bienvenido)
time.sleep(2)
print()
print("...")
time.sleep(0.3)
print()
print()
agenda = {}

def menu():
    time.sleep(0.3)
    print("1. Agregar contacto")
    time.sleep(0.3)
    print("2. Buscar contacto")
    time.sleep(0.3)
    print("3. Eliminar contacto")
    time.sleep(0.3)
    print("4. Mostrar todos los contactos")
    time.sleep(0.3)
    print("5. Salir")
    time.sleep(0.3)
    print()
    elección = input("Seleccione una opción (use el número): ")

def agregar_contacto():
    while True:
        print("desea agregar un contacto? (s/n)")
        opcion = input("> ")
        if opcion.lower() == "s":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado exitosamente.")
        elif opcion.lower() == "n":
            break
        else:
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")







menu()