class Cliente:
    """
    Clase base que representa a un cliente del sistema GIC.
    Contiene los atributos comunes a todos los tipos de cliente.
    """

    def __init__(self, nombre, email, telefono, direccion):
        """
        Inicializa un cliente con sus datos principales.
        """
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._direccion = direccion

    def get_email(self):
        return self._email

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}")
        print(f"Email: {self._email}")
        print(f"Teléfono: {self._telefono}")
        print(f"Dirección: {self._direccion}")

    def __str__(self):
        return f"{self._nombre} | {self._email}"
