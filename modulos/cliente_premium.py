from modulos.cliente import Cliente


class ClientePremium(Cliente):
    """
    Cliente premium con beneficios exclusivos.
    """

    def __init__(self, nombre, email, telefono, direccion, beneficios):
        super().__init__(nombre, email, telefono, direccion)
        self._beneficios = beneficios

    def beneficio_exclusivo(self):
        print("Acceso a soporte prioritario y descuentos especiales.")

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Cliente Premium")
        print(f"Beneficios: {self._beneficios}")
