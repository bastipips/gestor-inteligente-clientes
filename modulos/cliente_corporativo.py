from modulos.cliente import Cliente


class ClienteCorporativo(Cliente):
    """
    Cliente corporativo asociado a una empresa.
    """

    def __init__(self, nombre, email, telefono, direccion, empresa):
        super().__init__(nombre, email, telefono, direccion)
        self._empresa = empresa

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Cliente Corporativo")
        print(f"Empresa: {self._empresa}")
