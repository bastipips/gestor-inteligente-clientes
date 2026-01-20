import re
from modulos.excepciones import EmailInvalidoError, TelefonoInvalidoError


def validar_email(email):
    patron = r'^[\w\.-]+@gmail\.com$'
    if not re.match(patron, email):
        raise EmailInvalidoError("Email inválido. Debe ser @gmail.com")


def validar_telefono(telefono):
    if not telefono.isdigit() or len(telefono) != 9 or not telefono.startswith("9"):
        raise TelefonoInvalidoError(
            "Teléfono inválido. Debe tener 9 dígitos y comenzar con 9"
        )
