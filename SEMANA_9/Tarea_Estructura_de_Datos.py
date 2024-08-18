#clase producto


class Producto:
    def __init__(self, id_producto: object, nombre: object, cantidad: object, precio: object):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'{self.id_producto} {self.nombre} {self.cantidad} {self.precio}'

#clase inventario

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Se agregó un producto.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print('Se eliminó un producto')

    def actualizar_precio(self, id_producto, precio):
        for producto1 in self.productos:
            if producto1.id_producto == id_producto:
                producto1.precio = precio
                print('producto actualizado exitosamente')


    def buscar_producto(self, id_producto, nombre):
        for producto2 in self.productos:
            if producto2.id_producto == id_producto:
              producto2.nombre = nombre
              print('producto encontrado por su nombre')




    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)



mi_inventario: Inventario = Inventario()

"""""
producto1 = Producto(1, "manzana", 2, 3)
producto2 = Producto(2, "pera", 4, 2)

#print(producto.id)
#print(producto.nombre)

mi_inventario.agregar_producto(producto1)
mi_inventario.agregar_producto(producto2)

mi_inventario.mostrar_inventario()
mi_inventario.eliminar_producto(1)
mi_inventario.mostrar_inventario()

#actualización de precio

mi_inventario.actualizar_precio(2, 10)
mi_inventario.mostrar_inventario()

#buscar producto por nombre

mi_inventario.buscar_producto(2, "pera")
mi_inventario.mostrar_inventario()
"""""
def Menu():
    while True:
        print("Menu")
        print("1- Agregar producto")
        print("2- Eliminar un producto")
        print("3- Actualizar Producto")
        print("4- Encontrar prducto por su nombre")
        print("5- Mostrar Inventario")
        print("6- Salir")

        opcion =input("Opcion: ")
        if opcion == "1":
            id_producto= int(input("Ingrese el ID: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = int(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
if __name__ == "__main__":
    Menu()