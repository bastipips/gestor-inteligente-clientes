from modulos.cliente import Cliente


class ClienteRegular(Cliente):
    """
    Cliente regular del sistema.
    """

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Cliente Regular")
