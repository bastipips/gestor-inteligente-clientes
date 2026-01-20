from modulos.excepciones import ClienteExistenteError


class GestorClientes:
    """
    Clase encargada de administrar la colección de clientes.
    Permite agregar, listar y eliminar clientes.
    """
    def __init__(self):
        self._clientes = []

    def agregar_cliente(self, cliente):
        for c in self._clientes:
            if c.get_email() == cliente.get_email():
                raise ClienteExistenteError("El cliente ya existe.")

        self._clientes.append(cliente)

    def listar_clientes(self):
        for cliente in self._clientes:
            print("----------------------")
            cliente.mostrar_info()
            print("----------------------")
