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
    if elección == "1":
        agregar_contacto()
    elif elección == "2":
        buscar_contacto()
    elif elección == "3":
        eliminar_contacto()
    elif elección == "4":
        mostrar_contactos()
    elif elección == "5":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        menu()

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
            menu()
            break
        else:
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"El número de teléfono de '{nombre}' es: {agenda[nombre]}")
    else:
        print(f"Contacto '{nombre}' no encontrado en la agenda.")
    input()
    menu()

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado exitosamente.")
    else:
        print(f"Contacto '{nombre}' no encontrado en la agenda.")
    input()
    menu()

def mostrar_contactos():
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        print("Contactos en la agenda:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    input()
    menu()



menu()